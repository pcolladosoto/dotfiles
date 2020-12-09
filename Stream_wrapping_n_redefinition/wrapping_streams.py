import sys

class stream_wrapper:
    def __init__(self, stream_to_wrap = sys.stdout):
        print("Wrapping {}".format(sys.stdout.name))
        self.wrapped_stream = stream_to_wrap

    def write(self, inc):
        if inc in ['\n', ' ']:
            return
        # print(list(inc))
        # sys.stdout.flush()
        self.wrapped_stream.write(inc + " -- Printed from <wrapper> indeed!\n")
        # inc = "foo" + "faa\n"
        # self.wrapped_stream.write("foo" + "faa\n")

    # In case print() calls flush() on us!
    def flush(self):
        self.wrapped_stream.flush()

if __name__ == '__main__':
    wrapper = stream_wrapper()
    print("Printed this through <stdout>")
    print("Printed this through <wrapper>", file = wrapper)
    sys.stdout = wrapper
    print("Printed this through <wrapper>")
