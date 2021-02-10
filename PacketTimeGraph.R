setwd('C:/Users/ivan/Desktop')

library(ggplot2)
library(lattice)  
library(stringr)
library(frequency)
library(dplyr)

#UDP.csv file from folder CSV-03-11 in CIC-DDoS-2019 dataset
f="UDP.csv"
ds <- read.csv(f, stringsAsFactors=TRUE, header=T)
colnames(ds)

ds$Time <- as.numeric(as.POSIXct(ds$Time))

minimum = min(ds$Time, na.rm = FALSE)

ds$Time = ds$Time - minimum

step = 1
Tmax = ((floor(max(ds$Time, na.rm = TRUE)) + 5)/10)*10


ds_Packets = data.frame(ds$Time, 1, 1, ds$Label, 0, 0)
colnames(ds_Packets)=c("Time", "Time1", "nrPack", "Label", "UDP", "Attack")


ds_Packets$UDP <- ifelse(ds_Packets$Label %in% c("UDP"), 1, 0)
ds_Packets$Attack <- ifelse(ds_Packets$Label %in% c("MSSQL", "BENIGN"), 1, 0)


ds_Packets$Time1 = (ds_Packets$Time %/% step)*step

ds_final = aggregate(ds_Packets$nrPack, 
                    by=list(ds_Packets$Time1),   
                    FUN=sum, na.rm=TRUE)

ds_final2 = aggregate(ds_Packets$UDP, 
                     by=list(ds_Packets$Time1),   
                     FUN=sum, na.rm=TRUE)

ds_final3 = aggregate(ds_Packets$Attack, 
                      by=list(ds_Packets$Time1),   
                      FUN=sum, na.rm=TRUE)

colnames(ds_final)=c("Time", "Packets")
colnames(ds_final2)=c("Time", "Attack")
colnames(ds_final3)=c("Time", "NotAttack")


finalDS <- data.frame("Time" = ds_final$Time, 
                  "Packets" = ds_final$Packets, 
                  "Attack" =  ifelse(ds_final2$Attack > ds_final3$NotAttack, 1, 0)) 


plot(finalDS$Time, finalDS$Packets, main = "Packets/Time",
     xlab = "Time", ylab = "Number of Packets"   , xlim=c(0,Tmax), type = "l",
     frame = FALSE)


write.csv(finalDS,file="FINAL_data.csv")


