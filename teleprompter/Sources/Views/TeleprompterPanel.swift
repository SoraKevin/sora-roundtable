import AppKit

class TeleprompterPanel: NSPanel {

    private let state: TeleprompterState

    init(contentRect: NSRect, styleMask style: NSWindow.StyleMask, backing backingStoreType: NSWindow.BackingStoreType, defer flag: Bool) {
        let sharedState = TeleprompterState()
        self.state = sharedState

        super.init(
            contentRect: contentRect,
            styleMask: [.titled, .closable, .miniaturizable, .resizable],
            backing: backingStoreType,
            defer: flag
        )

        setupPanel()
    }

    private func setupPanel() {
        isFloatingPanel = false
        level = .normal
        becomesKeyOnlyIfNeeded = false
        isMovableByWindowBackground = true
        backgroundColor = NSColor.windowBackgroundColor
    }

    func setPinned(_ pinned: Bool) {
        level = pinned ? .floating : .normal
    }

    override var canBecomeKey: Bool { true }
    override var canBecomeMain: Bool { true }
}
