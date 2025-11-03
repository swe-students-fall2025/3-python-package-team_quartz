# pyflirt/data.py
BANK = {
    "nerdy": [
        {"text": "Are you made of copper and tellurium? Because you’re Cu-Te.", "cheese": 2},
        {"text": "Are you a quantum tunnel? Because you went straight through my barriers.", "cheese": 3},
        {"text": "Is your name Wi-Fi? Because I feel a strong connection.", "cheese": 3},
        {"text": "Are you a neural net, {name}? Because I keep overfitting to you.", "cheese": 4},
    ],
    "poetic": [
        {"text": "{name}, shall I compare thee to a stable release? Thou art rarer and far more dependable.", "cheese": 4},
        {"text": "I’d cross the version gulf for thee, and tag a release upon thy smile.", "cheese": 3},
    ],
    "cs": [
        {"text": "If love were a bug, I’d still refuse to close your ticket.", "cheese": 1},
        {"text": "Do you believe in love at first compile, {name}, or should I re-run?", "cheese": 2},
        {"text": "You must be Git—my heart commits to you.", "cheese": 2},
    ],
    "math": [
        {"text": "You must be my limit—I’m approaching you from every direction.", "cheese": 4},
        {"text": "If we were vectors, we’d be perfectly aligned.", "cheese": 2},
        {"text": "Are you √-1? You’re unreal—and I can’t stop imagining us.", "cheese": 4},
        {"text": "We are coprime; the only common divisor is one heart.", "cheese": 3},
    ],
    "classic": [
        {"text": "Are you a magician? Because whenever I look at you, everyone else disappears.", "cheese": 2},
    ],
}

def categories():
    return sorted(BANK.keys())
