import AppKit

class TeleprompterTextView: NSTextView {

    private var scrollTimer: Timer?
    private var state: TeleprompterState { TeleprompterState() }

    override init(frame frameRect: NSRect, textContainer container: NSTextContainer?) {
        super.init(frame: frameRect, textContainer: container)
        setup()
    }

    required init?(coder: NSCoder) {
        super.init(coder: coder)
        setup()
    }

    private func setup() {
        isEditable = true
        isSelectable = true
        isRichText = false
        font = NSFont.systemFont(ofSize: 24, weight: .medium)
        textColor = NSColor.labelColor
        backgroundColor = NSColor.textBackgroundColor
        insertionPointColor = NSColor.labelColor
        textContainerInset = NSSize(width: 16, height: 16)
        isVerticallyResizable = true
        isHorizontallyResizable = false
        autoresizingMask = [.width]
        textContainer?.widthTracksTextView = true
        textContainer?.heightTracksTextView = false
    }

    func startScrolling() {
        scrollTimer?.invalidate()
        guard state.speed > 0 else { return }

        let interval = 1.0 / 60.0  // 60 FPS
        scrollTimer = Timer.scheduledTimer(withTimeInterval: interval, repeats: true) { [weak self] _ in
            self?.scrollStep()
        }
    }

    func stopScrolling() {
        scrollTimer?.invalidate()
        scrollTimer = nil
    }

    private func scrollStep() {
        guard state.isScrolling else { return }
        let pixelsThisFrame = state.speed / 60.0
        let newY = visibleRect.origin.y - pixelsThisFrame
        scroll(to: NSPoint(x: 0, y: max(0, newY)))
        needsDisplay = true

        // Auto-stop at bottom
        if newY <= 0 {
            stopScrolling()
        }
    }

    override func keyDown(with event: NSEvent) {
        if event.keyCode == 49 {  // Space key
            toggleScrolling()
        } else {
            super.keyDown(with: event)
        }
    }

    private func toggleScrolling() {
        if state.isScrolling {
            stopScrolling()
        } else {
            startScrolling()
        }
    }
}
