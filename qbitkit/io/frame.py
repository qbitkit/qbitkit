import pandas as __pd__


class Frame:
    def get_frame(data=None):
        """Return a pandas DataFrame optionally populated with specified data from keyword arguments

        Args:
            data (dict): specify data to populate the Pandas DataFrame with. (default None)
        Returns:
            pandas.DataFrame: Empty DataFrame or dataframe populated with data specified using the 'data' keyword argument."""
        # Create and return a DataFrame from specified data.
        return __pd__.DataFrame(data=data)

    def fill_nan(input=get_frame(),
                 value=0):
        """Fill NaN values with a specified value.

        Args:
            input(pandas.DataFrame): DataFrame to Fill NaN values on. (default get_frame())
            value(int): Value to replace NaN values with. (default 0)
        Returns:
            pandas.DataFrame: DataFrame with NaN values replaced with the specified value."""
        # Return the DataFrame with NaN values replaced with the specified value.
        return input.fillna(value)
