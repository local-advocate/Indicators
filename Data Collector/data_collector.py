""" Input Argument for Data Collector Class"""
dataCollectorArg: dict = {
    "period": str,
    "interval": str,
    "ticker": str,
    "start": str,
    "end": str,
}

""" Variant values """
variant: dict = {
    "V1": 1,
    "V2": 2,
    "V3": 3,
    "V4": 4,
    "Invalid": -1,
}

""" Default values """
default: dict = {"variant": variant["Invalid"], "interval": "30M"}


""" Collects data within a given period and an interval of a given ticker. """


class DataCollector:

    """
    Arguments:
        from     :   start date, default today - interval
        end      :   end date, default today
        period   :   period till the current date
        interval :   1M, 5M, 30M, 1H, 2H, 4H, 1D, 1W, 1M, 1Y
        ticker   :   ticker of a company
    """

    def __init__(self, args: dataCollectorArg) -> None:
        self.variant = (
            args["variant"] if 'variant' in args else default["variant"]
        )  # Default variant 3
        self.interval = (
            args["interval"] if 'interval' in args else default["interval"]
        )  # Default interval '30M'
        self.args = args
        # continue: validate args, py dataframes, share mem, dataclasses etc.

    #
    # Decide what parameter to collect the data
    # Preference (highest to lowest):
    #     1. Start, Period (Variant 1)
    #     2. Period, End (Variant 2)
    #     3. Period (Variant 3)
    #     4. Start, End (Variant 4)
    #     5. Invalid (Variant 5)
    #

    def __variant(self) -> None:
        if 'period' in self.args:
            if 'start' in self.args:
                self.variant = variant["V1"]
            elif 'end' in self.args:
                self.variant = variant["V2"]
            else:
                self.variant = variant["V3"]
        elif 'start' in self.args and 'end' in self.args:
            self.variant = variant["V4"]
        else:
            self.variant = variant["Invalid"]


    def run(self) -> None:
        self.__variant()
        


if __name__ == "__main__":
    d = DataCollector(args={"period": ""})
    d.run()
