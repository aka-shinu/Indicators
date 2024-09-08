
# data = pandas data frame
data['Volume'] = data.Volume.round() * 68500
# for i in data:
#     print(i[-2])
#     time.sleep(1)
# exit()
prevdayHigh =  data['High'].max()
prevdayLow =  data['Low'].max()
prevdayClose = data['Close'].max()
def calcRs(n=14):
    loss=[]
    gain=[]
    for index, row in data.iterrows():
        r_2 = data.iloc[[index]]['Close'].item()
        if(index !=0):
           r_1 = data.iloc[[index-1]]['Close'].item()
           r_diff = r_2 - r_1
           if (r_diff) < 0:
               loss.append(-r_diff)
           else:
               gain.append(r_diff)
           if (index) == (n):
               break
            
    return gain, loss


def rma(source,periods):
    alpha = periods
    # (
    #   (
    #     int(
    #         1/periods
    #     )*source[0]) + (
    #         int(
    #             1 - (1/periods)
    #         )*source[1]
    #     )
    # )
    # return (((1/periods)*source[0]) +  ((1 - (1/periods))*source[1]))
    # return (
    #     ((
    #        (sum(source))/periods
    #     )*13) + source[0]
    # ) /  14
    # return ((
    #     ((sum(source)/periods) - 1)*((alpha-1)) + source[0]
    # )/alpha)  +source[0]
    return (
        sum(source)
    ) / periods
def calcPivot(n=1):
    return 

def calcEma(src,**kwargs):
    return src.ewm(**kwargs).mean()

def rsi(close, periods = 14):
    close_delta = close.diff()
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    ma_up = calcEma(up,com=periods, adjust=True, min_periods = periods)
    ma_down = calcEma(down,com=periods, adjust=True, min_periods = periods)
    rs = ma_up / ma_down
    rsi = 100 - (100/(1 + rs))
    return rsi




# print(rsi(data['Close'][::-1]))
# print(rsi(data['Close'][::-1]).max())

pivotPoint1 = calcPivot(0)
pivotPoint2 = calcPivot(1)
data['H/L'] = np.NAN
data['max'] = 0
data['min'] = 0
def sort(data, clmn):
    return data.sort_values(by=[clmn], ascending=True)
    

def markMaximaMinima(data: pd.DataFrame):
    for index, row in data.iterrows():
        if index:
            e2 = data.iloc[[index+1]]['High'].item()
            Me2 = data.iloc[[index+2]]['High'].item()
            e1 = data.iloc[[index-1]]['High'].item()
            Me1 = data.iloc[[index-2]]['High'].item()
            m = data.iloc[[index]]['High'].item()
            e2_ = data.iloc[[index+1]]['Low'].item()
            Me2_ = data.iloc[[index+2]]['Low'].item()
            e1_ = data.iloc[[index-1]]['Low'].item()
            Me1_ = data.iloc[[index-2]]['Low'].item()
            m = data.iloc[[index]]['High'].item()
            m_ = data.iloc[[index]]['Low'].item()
            if m>e2:
             if m>e1:
              if m > Me2:
               if m>Me1:
                   data.loc[index, "H/L"] = "H"
                   data.loc[index, "max"] = m
            if m_<e2_:
             if m_<e1_:
              if m_ < Me2_:
               if m_<Me1_:
                   data.loc[index, "H/L"] = "L"
                   data.loc[index, "min"] = m_
# exit()        
# try:
#     markMaximaMinima(data)
#    macd
    print(calcEma(data['Close'][::-1], span=12, adjust=False) - calcEma(data['Close'][::-1], span=26, adjust=False))
#  ##;
# except:
#     pass
# stoc
# print(
#     ( data.iloc[[0]]['Close'].item() - data.loc[0:14]['min'].max()) / (data.loc[0:14]['max'].max() - data.loc[0:14]['min'].max())*100
# )
# print(data.to_string())

d = data.loc[0:14]
typicalPrice = (d.sum() + d.sum() + d.sum()) / 3
def mad(x,):
 s=0
 k=0
 n=len(x.values)
 print(x.values)
 tp = (data.loc[data['sma'] == x.values[-1]])['tp'].item()
 print(x)
 for i in range(n-1):
    try:
      s += int(tp) - int(x.values[n-1-i]) 
      k+=1
    except Exception:
        break
#  return s/k
 return x.sum()
from numpy import mean, absolute

def mad(data, axis=None):
    return mean(absolute(data - mean(data, axis)), axis)


def CCI(df: pd.DataFrame, ndays=20): 
    df['tp'] = (df['High'] + df['Low'] + df['Close']) / 3
    df['sma'] = df.tp[::-1].rolling(ndays).mean()[::-1]
    df['mad'] = df.tp[::-1].rolling(ndays).apply(lambda x: mad(x))
    df['CCI'] = (df.tp -df.sma) / (df.mad*.015 )
    return data

def momentum(df, period=20):
   for index, row in df.iterrows():
       curClose = df.iloc[[index]].Close.item()
       nAgo = df.loc[index: period+index].iloc[[-1]].Close.item()
       df.loc[index, "mom"] = curClose - nAgo
       if (period-1) == index:
           break
   return df


def obv(df: pd.DataFrame, period=20):
    df2 = df.loc[0:10][::-1]
    k=0
    for index, row in df2.iterrows():
      if not(k):
          df.loc[index, 'obv'] =  0
          k += 1
      else:
        prevObv = row.shift(1).Volume
        todVol  = row.Volume
        todaysClosing = row.Close
        yestClosing = row.shift(1).Close
        if todaysClosing>yestClosing:
            df.loc[index, 'obv'] = prevObv + (todVol)
        elif todaysClosing<yestClosing:
            df.loc[index, 'obv'] = prevObv - (todVol)
        elif todaysClosing == yestClosing:
            df.loc[index, 'obv']= prevObv
    return df

def vwma(df):
    tw= calcEma(df['cxv'],span=12, adjust=False) / calcEma(df['Volume'],span=12, adjust=False)
    ts = calcEma(df['cxv'], span=26, adjust=False) / calcEma(df['Volume'], span=26, adjust=False)
    return tw-ts
    # if n == 11:
    #     if(i) == (n):
    #       return vwma(df,c,25)
    #     return vwma(df,c, n, i+1)
    # if(i) == (n):
    #  return df
    # return vwma(df,c,n,i+1)
try:
    
 markMaximaMinima(data)
except:
    pass
# data['cxv'] = data.Close*data.Volume
obv(data)
# data = vwma(data[::-1])
# data['vwmacd'] = data['vwma12'] - data['vwma26']

# data['rawMoneyFlow'] = data.tp*data.Volume

def calcMFI(origdata: pd.DataFrame, ndata: pd.DataFrame=None, period=14,i=0,calcLower=False, upper=[], lower=[]):
    try:
        
        if  ndata == None:
            ndata=origdata
    except ValueError:
        pass
    n_up=0
    n_low = 0
    for index, row in ndata.iterrows():
        change = -ndata.iloc[[index+1-i]].tp.item() + row.tp
        sign = math.copysign(1, change)
        if n_up == (period):
            origdata.loc[index-period,'mfi'] = 100 - (100/(1 + sum(upper) / sum(lower)))
            if (i==period):
             return origdata    
            return calcMFI(origdata=origdata, ndata=origdata.loc[i+1:], i=i+1,upper=[],lower=[])
        if(sign==-1):
           lower.append(row.tpxV)
           n_low += 1
        if(sign) == 1:
            upper.append(row.tpxV)
        n_up+=1
            
            
data['MFM']  = ((data.Close - data.Low) - (data.High - data.Close)) / (data.High-data.Low)
data['MFV'] = data.MFM * data.Volume


def calculateCMF(origData: pd.DataFrame ,i=0):
    s=origData.loc[i: 19+i]
    origData.loc[i, "CMF"] = (s.MFV.sum() / s.Volume.sum()).round(2)
    if (i==10):
        return origData
    return calculateCMF(origData, i+1)

def calculatemacdHIST(origData,i=0):
    origData['macd']=(calcEma(origData['Close'][::-1], span=12, adjust=False) - calcEma(origData['Close'][::-1], span=26, adjust=False))[::-1]
    origData['signalLine'] = calcEma(origData['macd'][::-1],span=9, adjust=False)[::-1]
    origData['HIST'] = origData.macd - origData.signalLine
    return origData