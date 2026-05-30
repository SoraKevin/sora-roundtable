#!/usr/bin/env python3
"""
Merge 7 academic research agent files for Distiller-DNA-by-Sora.
Outputs a compact Phase 1.5 review table with mode-readiness signals.

Usage:
    python3 merge_research.py <skill_dir>
"""
import re
import sys
from pathlib import Path

AGENTS = {
    '01-paper-corpus': 'Paper Corpus',
    '02-method-dna': 'Method DNA',
    '03-writing-dna': 'Writing DNA',
    '04-talks-interviews': 'Talks/Interviews',
    '05-peer-reception': 'Peer Reception',
    '06-lineage-timeline': 'Lineage/Timeline',
    '07-artifacts-code-data': 'Artifacts/Code/Data',
}


def count_sources(content: str):
    urls = re.findall(r'https?://[^\s\)]+', content)
    dois = re.findall(r'\b10\.\d{4,9}/[-._;()/:A-Z0-9]+', content, re.I)
    arxiv = re.findall(r'arXiv[:\s]*\d{4}\.\d{4,5}', content, re.I)
    primary = len(re.findall(r'primary|一手|作者本人|official|paper|preprint|repo|talk', content, re.I))
    secondary = len(re.findall(r'secondary|二手|survey|peer|review|replication|commentary', content, re.I))
    inferred = len(re.findall(r'inferred|推断', content, re.I))
    return {
        'sources': len(set(urls)) + len(set(dois)) + len(set(arxiv)),
        'primary': primary,
        'secondary': secondary,
        'inferred': inferred,
    }


def extract_findings(content: str, n=2):
    bullets = re.findall(r'^[-*]\s+(.+)$', content, re.M)
    heads = re.findall(r'^##\s+(.+)$', content, re.M)
    items = bullets or heads
    return '; '.join([x[:60] for x in items[:n]]) or '—'


def readiness(files):
    merged = '\n'.join(files.values())
    kernel = bool(re.search(r'DNA Kernel|Primitive|Research DNA|排他|独特', merged, re.I))
    open_fw = bool(re.search(r'Open Framework|Evolution|Tension|Open Problems|演化|张力|开放问题', merged, re.I))
    negative = bool(re.search(r'criticism|failure|replication|negative|质疑|批评|复现失败', merged, re.I))
    recent = bool(re.search(r'202[5-9]|近\s*12\s*个月|latest|recent', merged, re.I))
    return kernel, open_fw, negative, recent


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 merge_research.py <skill_dir>')
        sys.exit(1)
    skill_dir = Path(sys.argv[1])
    research_dir = skill_dir / 'references' / 'research'
    if not research_dir.exists():
        print(f'❌ missing research dir: {research_dir}')
        sys.exit(1)

    files = {}
    total_sources = total_primary = total_secondary = total_inferred = 0
    rows = []
    missing = []
    for stem, label in AGENTS.items():
        path = research_dir / f'{stem}.md'
        if not path.exists():
            missing.append(label)
            rows.append((label, '❌ missing', '—'))
            continue
        content = path.read_text(encoding='utf-8')
        files[stem] = content
        stats = count_sources(content)
        total_sources += stats['sources']
        total_primary += stats['primary']
        total_secondary += stats['secondary']
        total_inferred += stats['inferred']
        rows.append((label, str(stats['sources']), extract_findings(content)))

    print('| Agent | Sources | Key findings |')
    print('|---|---:|---|')
    for label, sources, findings in rows:
        print(f'| {label} | {sources} | {findings} |')
    print('| **Total** | **{}** | primary markers: {}; secondary markers: {}; inferred markers: {} |'.format(
        total_sources, total_primary, total_secondary, total_inferred))

    kernel, open_fw, negative, recent = readiness(files)
    print('\n## Mode readiness')
    print(f'- DNA Kernel readiness: {"✅" if kernel else "⚠️"}')
    print(f'- Open Framework readiness: {"✅" if open_fw else "⚠️"}')
    print(f'- Negative evidence / criticism coverage: {"✅" if negative else "⚠️"}')
    print(f'- Recent-work coverage signal: {"✅" if recent else "⚠️"}')
    if missing:
        print(f'\n⚠️ Missing dimensions: {", ".join(missing)}')
    if total_sources < 10:
        print('\n⚠️ Total source count is low; downgrade to lightweight DNA or request more materials.')


if __name__ == '__main__':
    main()
