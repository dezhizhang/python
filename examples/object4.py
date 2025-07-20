

class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)


clock = Clock()
clock.id = "20300"
clock.price = 19.99

clock.ring()


