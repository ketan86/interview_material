# pylint: skip-file
class Target():
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is 
    incompatible with the existing client code. The Adaptee needs 
    some adaptation before the client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


# print("Client: I can work just fine with the Target objects:")
# target = Target()
# client_code(target)
# print("\n")

# adaptee = Adaptee()
# print("Client: The Adaptee class has a weird interface. "
#       "See, I don't understand it:")
# print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

# print("Client: But I can work with it via the Adapter:")
# adapter = Adapter(adaptee)
# client_code(adapter)


"""
// Say you have two classes with compatible interfaces:
// RoundHole and RoundPeg.
class RoundHole is
    constructor RoundHole(radius) { ... }

    method getRadius() is
        // Return the radius of the hole.

    method fits(peg: RoundPeg) is
        return this.getRadius() >= peg.radius()

class RoundPeg is
    constructor RoundPeg(radius) { ... }

    method getRadius() is
        // Return the radius of the peg.


// But there's an incompatible class: SquarePeg.
class SquarePeg is
    constructor SquarePeg(width) { ... }

    method getWidth() is
        // Return the square peg width.


// An adapter class lets you fit square pegs into round holes.
// It extends the RoundPeg class to let the adapter objects act
// as round pegs.
class SquarePegAdapter extends RoundPeg is
    // In reality, the adapter contains an instance of the
    // SquarePeg class.
    private field peg: SquarePeg

    constructor SquarePegAdapter(peg: SquarePeg) is
        this.peg = peg

    method getRadius() is
        // The adapter pretends that it's a round peg with a
        // radius that could fit the square peg that the adapter
        // actually wraps.
        return peg.getWidth() * Math.sqrt(2) / 2


// Somewhere in client code.
hole = new RoundHole(5)
rpeg = new RoundPeg(5)
hole.fits(rpeg) // true

small_sqpeg = new SquarePeg(5)
large_sqpeg = new SquarePeg(10)
hole.fits(small_sqpeg) // this won't compile (incompatible types)

small_sqpeg_adapter = new SquarePegAdapter(small_sqpeg)
large_sqpeg_adapter = new SquarePegAdapter(large_sqpeg)
hole.fits(small_sqpeg_adapter) // true
hole.fits(large_sqpeg_adapter) // false
"""


class RoundHole:
    _redius = 2

    def fits(self, peg):
        if peg.radius < self._redius:
            print('can not fit peg')
        else:
            print('peg fits well')


class RoundPeg:
    radius = 2


class SquarePeg:
    width = 1
    depth = 1


class SquarePegAdapter(RoundHole):

    def __init__(self, peg):
        self.peg = peg
        self.radius = peg.width * 2


hole = RoundHole()
rpeg = RoundPeg()
speg = SquarePeg()
speg_adp = SquarePegAdapter(speg)
hole.fits(rpeg)
hole.fits(speg_adp)
