# MOVING-AVERAGE-CONVERGENCE-DIVERGENCE-MACD-TDI-PAC-Heikin-Ashi-V.2.5
This is a trend trading indicator and alert that utilizes the Traders Dynamic Index ( TDI ), Price Action Channel (PAC) and Heikin Ashi candles.

About 6months ago I came across the use of TDI in "E.A.S.Y. Method" that I found in forexfactory forums: http://www.forexfactory.com/attachment.p...
and I was able to set up a chart based on the specifications by using Kurbelklaus scripts. However, I found that the alerts were being generated one or two bars too late, so at that time I was not successful using it with Binary Options. A few months later I found a variation of the method in the forecfactory forums which is able to generate the alerts a bit earlier, so this indicator is a modification of that early detection version.

The indicator can optionally use Heikin Ashi candles only for all it's calculation. I would recommend viewing the chart with Heikin Ashi candles, these smooth out the trends and makes trends very clear.

I found that this method it works good with most currency pairs or commodities and with 5min+ timeframe charts. I would suggest expiry of 2 to 6 candles.

ALERT GENERATION:
=================

The TDI (Traders Dynamic Index)
---------------------------------------------
Volatility Band VB (34), color: Blue, buffer: UpZone, DnZone
Relative Strength Index RSI (13)
RSI PRICE LINE ( 2 ), color: Green, buffer: mab
RSI TRADE SIGNAL LINE (7), color: Red, buffer: mbb
MARKET BASE LINE MID VB (34), color: Orange, buffer: mid

Indicator SignalLevels:
-------------------------------
RSI_OversoldLevel : 22 (normally: 32)
RSI_OverboughtLevel : 78 (normally: 68)

Alert Conditions:
-----------------------
Strong Buy : yellow
Medium Buy : aqua
Weak Buy : blue

Strong Sell : fuchsia
Medium Sell : purple
Weak Sell : black

Hints on How to use:
----------------------------
- When a Medium or Strong alert is generated and MACD histogram colour matches the direction
of the alert (optional auto filter), then place trade in direction of alert candle and MACD .
- I use the multi-Hull MA's for overall trend direction confirmation.
- Best positions normally occur near the MACD (5,15,1) Histogram crossing the zero line.
- The optional coloured Dots along the bottom of the indicator represent the first alert
of this type that was generated in this sequence.
- It is advisable to trade in the direction of the main trend as indicated the HULL MA red cloud:
if red cloud underneath PAC then BULLISH trend , if red cloud above PAC then BEARISH trend .
- Selecting the HeiKin Ashi candles does affect the MACD and MA caculations, so if you select
normal candles the result chart will change. You can still Optionally select to use Heikin Ashi
for calculations.
- When using the Heikin Ashi candles, a good buy entry is indicated by long top wick and no bottom wick
for bull (green) candles and good sell entry is indicated by long bottom wick and no top wick for
bear (red) candles.
- When the MACD histogram is flat and close to zero line,
this indicates a ranging market, do NOT trade when this occurs.
- When the PAC channel on the main chart is spread apart widely, this is an indication
of extreme volatility and choppy chart, do NOT try to trade during these periods.
A choppy chart is also indicated by Heikin Ashi candles with long wicks on both sides
of the candles.
- You can specify what strength level Alerts are generated (default 2 ):
Level (1) means only generate Strong Alerts only.
Level ( 2 ) means generate Strong and Medium Alerts.
Level (3) means generate Strong, Medium and Weak Alerts.
