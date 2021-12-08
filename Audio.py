import random
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import pyaudio


# own address 127.0.0.1

class Client(DatagramProtocol):
    # to start the protocol
    def startProtocol(self):
        audio = pyaudio.PyAudio()
        # amount of frames in the buffer
        self.buffer = 2048
        self.secondClient = input("Write address: "), int(input("Port: "))
        # rate/sampling = fps
        self.output_stream = audio.open(format=pyaudio.paInt16, output=True, rate=44100, channels=2,
                                        frames_per_buffer=self.buffer)

        self.input_stream = audio.open(format=pyaudio.paInt16, input=True, rate=44100, channels=1,
                                       frames_per_buffer=self.buffer)
        # split program in threads
        reactor.callInThread(self.record())

    # when we speak, takes voice
    def record(self):
        # while someone is talking for how ever long
        while True:
            data = self.input_stream.read(self.buffer)
            # display data in console of sounds
            print(data)
            # send data to another client
            self.transport.write(data, self.secondClient)

    # receive address, port, and data and output
    def datagramReceived(self, datagram, addr):
        self.output_stream.write(datagram)


if __name__ == '__main__':
    port = random.randint(1000, 3000)
    print("Working on port", port)

    # listening in on the port, initialize client
    reactor.listenUDP(port, Client())
    # run the reactor
    reactor.run()
