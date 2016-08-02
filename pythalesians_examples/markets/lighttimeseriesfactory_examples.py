__author__ = 'saeedamen' # Saeed Amen / saeed@thalesians.com

#
# Copyright 2015 Thalesians Ltd. - http//www.thalesians.com / @thalesians
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and limitations under the License.
#

"""
lightimeseriesfactory_examples

Gives several examples of how to download market data from external sources like Bloomberg using LightTimeSeriesFactory.
Also uses PlotFactory to do basic plots.

"""

# for logging
from pythalesians.util.loggermanager import LoggerManager

from pythalesians.market.loaders.lighttimeseriesfactory import LightTimeSeriesFactory
from pythalesians.market.requests.timeseriesrequest import TimeSeriesRequest
from pythalesians.timeseries.calcs.timeseriescalcs import TimeSeriesCalcs

from chartesians.graphs.graphproperties import GraphProperties
from chartesians.graphs.plotfactory import PlotFactory

if True:
    logger = LoggerManager().getLogger(__name__)

    import datetime

    # just change "False" to "True" to run any of the below examples

    ###### download daily data from Bloomberg for EUR/USD and GBP/USD spot and then plot
    if False:

        time_series_request = TimeSeriesRequest(
                start_date = "01 Jan 2014",                     # start date
                finish_date = datetime.date.today(),            # finish date
                freq = 'daily',                                 # daily data
                data_source = 'bloomberg',                      # use Bloomberg as data source
                tickers = ['EURUSD',                            # ticker (Thalesians)
                           'GBPUSD'],
                fields = ['close', 'high', 'low'],              # which fields to download
                vendor_tickers = ['EURUSD BGN Curncy',          # ticker (Bloomberg)
                                  'GBPUSD BGN Curncy'],
                vendor_fields = ['PX_LAST', 'PX_HIGH', 'PX_LOW'],   # which Bloomberg fields to download
                cache_algo = 'internet_load_return')                # how to return data

        ltsf = LightTimeSeriesFactory()

        df = None
        df = ltsf.harvest_time_series(time_series_request)

        pf = PlotFactory()
        pf.plot_line_graph(df, adapter = 'pythalesians')

    ###### download event dates for non farm payrolls and then print
    if False:

        time_series_request = TimeSeriesRequest(
                start_date = "01 Jan 2014",                     # start date
                finish_date = datetime.date.today(),            # finish date
                category = "events",
                freq = 'daily',                                 # daily data
                data_source = 'bloomberg',                      # use Bloomberg as data source
                tickers = ['FOMC', 'NFP'],
                fields = ['release-date-time-full', 'release-dt', 'actual-release'],                    # which fields to download
                vendor_tickers = ['FDTR Index', 'NFP TCH Index'],                                       # ticker (Bloomberg)
                vendor_fields = ['ECO_FUTURE_RELEASE_DATE_LIST', 'ECO_RELEASE_DT', 'ACTUAL_RELEASE'],   # which Bloomberg fields to download
                cache_algo = 'internet_load_return')                # how to return data

        ltsf = LightTimeSeriesFactory()

        df = None
        df = ltsf.harvest_time_series(time_series_request)

        print(df)

    ###### download daily data from Bloomberg for 30Y DE bonds and then plot
    if False:

        time_series_request = TimeSeriesRequest(
                start_date = "01 Jan 1990",                     # start date
                finish_date = datetime.date.today(),            # finish date
                freq = 'daily',                                 # daily data
                data_source = 'bloomberg',                      # use Bloomberg as data source
                tickers = ['DE 30Y Bond'],                      # ticker (Thalesians)
                fields = ['close', 'high', 'low', 'open'],                          # which fields to download
                vendor_tickers = ['UB1 Comdty'],                # ticker (Bloomberg)
                vendor_fields = ['PX_LAST', 'PX_HIGH', 'PX_LOW', 'PX_OPEN'],        # which Bloomberg fields to download
                cache_algo = 'internet_load_return')            # how to return data

        ltsf = LightTimeSeriesFactory()

        df = None
        df = ltsf.harvest_time_series(time_series_request)

        pf = PlotFactory()
        pf.plot_line_graph(df, adapter = 'pythalesians')

    ###### download intraday data from Bloomberg for EUR/USD and GBP/USD spot and then plot
    if False:
        from datetime import timedelta
        start_date = datetime.datetime.utcnow() - timedelta(days=1)

        time_series_request = TimeSeriesRequest(
                start_date = start_date,         # start date
                finish_date = datetime.datetime.utcnow(),                       # finish date
                freq = 'intraday',                                              # intraday data
                data_source = 'bloomberg',                      # use Bloomberg as data source
                tickers = ['EURUSD',                            # ticker (Thalesians)
                           'GBPUSD',
                           'JPYUSD',
                           'AUDUSD'],
                fields = ['close'],                             # which fields to download
                vendor_tickers = ['EURUSD BGN Curncy',          # ticker (Bloomberg)
                                  'GBPUSD BGN Curncy',
                                  'JPYUSD BGN Curncy',
                                  'AUDUSD BGN Curncy'],
                vendor_fields = ['close'],                    # which Bloomberg fields to download
                cache_algo = 'internet_load_return')            # how to return data

        ltsf = LightTimeSeriesFactory()

        df = ltsf.harvest_time_series(time_series_request)
        df.columns = [x.replace('.close', '') for x in df.columns.values]

        gp = GraphProperties()
        pf = PlotFactory()
        gp.source = 'Thalesians/BBG (created with PyThalesians Python library)'

        tsc = TimeSeriesCalcs()
        df = tsc.create_mult_index_from_prices(df)

        pf.plot_line_graph(df, adapter = 'pythalesians', gp = gp)

    ###### download daily data from Quandl (via FRED) for EUR/USD and GBP/USD spot and then plot
    if False:

        time_series_request = TimeSeriesRequest(
                start_date = "01 Jan 1970",                     # start date
                finish_date = datetime.date.today(),            # finish date
                freq = 'daily',                                 # daily data
                data_source = 'quandl',                         # use Quandl as data source
                tickers = ['EURUSD',                            # ticker (Thalesians)
                           'GBPUSD'],
                fields = ['close'],                                 # which fields to download
                vendor_tickers = ['FRED/DEXUSEU', 'FRED/DEXUSUK'],  # ticker (Quandl)
                vendor_fields = ['close'],                          # which Bloomberg fields to download
                cache_algo = 'internet_load_return')                # how to return data

        ltsf = LightTimeSeriesFactory()

        df = ltsf.harvest_time_series(time_series_request)

        pf = PlotFactory()
        pf.plot_line_graph(df, adapter = 'pythalesians')

    ###### download CPI data from FRED
    if False:

        time_series_request = TimeSeriesRequest(
                start_date = "01 Jan 1970",                     # start date
                finish_date = datetime.date.today(),            # finish date
                freq = 'daily',                                 # daily data
                data_source = 'fred',                           # use FRED as data source
                tickers = ['US CPI YoY', 'EZ CPI YoY'],         # ticker (Thalesians)
                fields = ['close'],                                 # which fields to download
                vendor_tickers = ['CPIAUCSL', 'CP0000EZ17M086NEST'],                     # ticker (Yahoo)
                vendor_fields = ['Close'],                          # which Bloomberg fields to download
                cache_algo = 'internet_load_return')                # how to return data

        ltsf = LightTimeSeriesFactory()

        df = ltsf.harvest_time_series(time_series_request)

        # calculate YoY data
        df = df / df.shift(12) - 1

        pf = PlotFactory()
        pf.plot_line_graph(df, adapter = 'pythalesians')

    ###### download daily data from Yahoo for Apple and Citigroup stock and then plot
    if False:

        time_series_request = TimeSeriesRequest(
                start_date = "01 Jan 1970",                     # start date
                finish_date = datetime.date.today(),            # finish date
                freq = 'daily',                                 # daily data
                data_source = 'yahoo',                          # use Bloomberg as data source
                tickers = ['Apple', 'Citigroup'],                   # ticker (Thalesians)
                fields = ['close'],                                 # which fields to download
                vendor_tickers = ['aapl', 'c'],                     # ticker (Yahoo)
                vendor_fields = ['Close'],                          # which Bloomberg fields to download
                cache_algo = 'internet_load_return')                # how to return data

        ltsf = LightTimeSeriesFactory()

        df = ltsf.harvest_time_series(time_series_request)

        pf = PlotFactory()
        pf.plot_line_graph(df, adapter = 'pythalesians')

    # downloading historical tick data from Dukascopy broker for EUR/USD
    # (past month of data cannot be downloaded, hence cannot be used for live trading)
    if True:
        time_series_request = TimeSeriesRequest(
                start_date = "01 Jun 2015",                     # start date
                finish_date = "02 Jun 2015",                    # finish date
                freq = 'tick',                                  # tick data
                data_source = 'dukascopy',                      # use dukascopy as data source
                tickers = ['EURUSD', 'GBPUSD'],                 # ticker (Thalesians)
                fields = ['bid', 'ask'],                        # which fields to download
                vendor_tickers = ['EURUSD', 'GBPUSD'],          # ticker (Dukascopy)
                vendor_fields = ['bid', 'ask'],                 # which Dukascopy fields to download
                cache_algo = 'internet_load_return')            # how to return data

        ltsf = LightTimeSeriesFactory()

        df = ltsf.harvest_time_series(time_series_request)

        gp = GraphProperties()
        gp.y_axis_2_series = ['GBPUSD.bid', 'GBPUSD.ask']

        pf = PlotFactory()
        pf.plot_line_graph(df, adapter = 'pythalesians', gp = gp)

    ###### download daily data from Google for Apple and S&P500 ETF (and then rebase, before plotting)
    if False:

        time_series_request = TimeSeriesRequest(
                start_date = "01 Jan 1970",                     # start date
                finish_date = datetime.date.today(),            # finish date
                freq = 'daily',                                 # daily data
                data_source = 'google',                          # use Bloomberg as data source
                tickers = ['Apple', 'S&P500 ETF'],                  # ticker (Thalesians)
                fields = ['close'],                                 # which fields to download
                vendor_tickers = ['aapl', 'spy'],                   # ticker (Google)
                vendor_fields = ['Close'],                          # which Bloomberg fields to download
                cache_algo = 'internet_load_return')                # how to return data

        ltsf = LightTimeSeriesFactory()
        tsc = TimeSeriesCalcs()

        df = tsc.create_mult_index_from_prices(ltsf.harvest_time_series(time_series_request))

        pf = PlotFactory()
        pf.plot_line_graph(df, adapter = 'pythalesians')

