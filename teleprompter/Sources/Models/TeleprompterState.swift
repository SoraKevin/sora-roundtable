import Foundation

class TeleprompterState: ObservableObject {

    @Published var opacity: Double = 0.85
    @Published var speed: Double = 50.0  // pixels per second
    @Published var isScrolling: Bool = false
    @Published var isPinned: Bool = false

    static let minOpacity: Double = 0.1
    static let maxOpacity: Double = 1.0
    static let minSpeed: Double = 10.0
    static let maxSpeed: Double = 200.0

    func increaseOpacity(by delta: Double = 0.05) {
        opacity = min(maxOpacity, opacity + delta)
    }

    func decreaseOpacity(by delta: Double = 0.05) {
        opacity = max(minOpacity, opacity - delta)
    }

    func increaseSpeed(by delta: Double = 10.0) {
        speed = min(maxSpeed, speed + delta)
    }

    func decreaseSpeed(by delta: Double = 10.0) {
        speed = max(minSpeed, speed - delta)
    }
}