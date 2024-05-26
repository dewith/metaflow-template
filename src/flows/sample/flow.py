""""Sample flow"""

from metaflow import FlowSpec, step


class SampleFlow(FlowSpec):
    """Sample flow"""

    # pylint: disable=attribute-defined-outside-init
    # pylint: disable=import-outside-toplevel
    # pylint: disable=too-many-instance-attributes

    @step
    def start(self):
        """Start the flow"""
        self.text = "Hello, World!"
        self.next(self.end)

    @step
    def end(self):
        """End the flow"""
        print(self.text)


if __name__ == "__main__":
    SampleFlow()
