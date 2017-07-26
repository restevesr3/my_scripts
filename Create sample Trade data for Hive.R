# Task: Create sample Trade data for use with Apache Hive Queries
# Author: Robert Esteves
# Programming Language: R-Programming


company_df<-data.frame(symbol=c('GOOG', 'APPL', 'MSFT', 'FB', 'SNAP', 'TWTR', 'CSCO'),
                       company=c('Google', 'Apple', 'Microsoft','Facebook', 'SNAP Inc', 'Twitter', 'Cisco'),
                       stringsAsFactors = FALSE
                       
                       )

head(company_df)

company_df[1,1]

trades.list<-list()

trades.list

for(i in 1:nrow(company_df)){
  #print(i)
  
  company_symbol<-company_df[i,1]
  company_name<-company_df[i,2]
  symbol<-rep(company_symbol, 10)
  name<-rep(company_name, 10)
  trade.open<-rnorm(10, mean = 400, sd=100)
  trade.high<-rnorm(10, mean=400, sd=50)
  trade.low<-rnorm(10, mean=350, sd=40)
  trade.close<-rnorm(10, mean=400, sd=80)
  sd<-as.Date('2017-01-01')
  calendar.date<-seq(from=sd, by="day", length.out = 10)
  df<-data.frame(symbol=symbol, 
                 company=name, 
                 open=trade.open, 
                 high=trade.high, 
                 low=trade.low, 
                 close=trade.close,
                 date=calendar.date)
  #print(df)
  trades.list[[company_name]]<-df
  
}

trades.list

trades_df<-do.call('rbind',trades.list)

trades_df

rownames(trades_df)<-NULL

trades_df

write.table(trades_df, 
            '/xxxxxx/sf_Virtual_NAS_Drive/Hive Test Files/TRADES.csv',
            sep='|',
            row.names = FALSE,
            quote = FALSE,
            col.names = FALSE
            )
