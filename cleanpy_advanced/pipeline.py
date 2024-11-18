class CleaningPipeline:
    """
    Custom cleaning pipeline to chain operations.
    """

    def __init__(self):
        self.steps = []

    def add_step(self, func, *args, **kwargs):
        """
        Add a cleaning step to the pipeline.

        Parameters:
            func (callable): Cleaning function.
            *args: Positional arguments for the function.
            **kwargs: Keyword arguments for the function.
        """
        self.steps.append((func, args, kwargs))

    def run(self, df):
        """
        Run the pipeline on a DataFrame.

        Parameters:
            df (pd.DataFrame): The DataFrame to process.

        Returns:
            pd.DataFrame: The cleaned DataFrame.
        """
        for func, args, kwargs in self.steps:
            df = func(df, *args, **kwargs)
        return df
