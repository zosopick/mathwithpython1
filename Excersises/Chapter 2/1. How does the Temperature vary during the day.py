'''
Write a program that compares 24h weather predictions of two citires on the same graph.
Time of day on the x-axis and the temperature reading on the y-axis.
'''
from pylab import plot, show, legend, title , xlabel, ylabel


weather_tuzla=(7,6,4,3,2,2,0,1,2,5,9,12,13,14,15,15,16,14,14,12,11,10,7,6)
weather_vienna=[7,6,5,6,4,3,2,4,5,7,10,11,13,14,15,16,15,14,14,13,11,9,8,7]


time=('12AM', '1AM', '2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12PM','1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM')
plot(time,weather_tuzla,time,weather_vienna,marker='o')
title('Weather in Tuzla, BiH and Vienna,Austria  on saturday the 3.4.2020')
xlabel('Time of day')
ylabel('Temperaure reading')
legend(['Tuzla','Vienna'])


show()
