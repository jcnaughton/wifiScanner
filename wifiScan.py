import subprocess
import re
import os

def getStats():
    output = subprocess.check_output(["tail","/proc/net/wireless"])
    m = re.search("wlan0\:\s+0000\s+(?P<link>\d{1,2})\.\s+-(?P<level>\d{1,2})\.\s+-(?P<noise>\d{1,3})",output.decode("utf-8"))
    return(m.groupdict())

linkList = []
levelList = []
noiseList = []
locationList = []
columns = ['location','link','level','noise']
locationList.append(columns)


for location in range(1,30):
    stop = input("Move Station to location number " + str(location) + " then hit enter")
    getStatsDict = getStats()
    signalList = [str(location)]
    for key in getStatsDict.keys():
        signalList.append(int(getStatsDict[key]))
    locationList.append(signalList)

f=open("index.html","w")
html = '<html><head><script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>\n'
html += '<script type="text/javascript">\n'
html += "      google.charts.load('current', {'packages':['corechart','line']});\n"
html += 'google.charts.setOnLoadCallback(drawChart);\n'
html += 'function drawChart() {\n'
html += 'var data = google.visualization.arrayToDataTable('
html += str(locationList)
html += ");\n"
html += "      var options = {\n"
html += "        chart: \n{"
html += "          title: 'Wifi Signal',\n"
html += "        }\n,"
html += "        width: 900,\n"
html += "        height: 500\n"
html += "      };\n"
html += "var chart = new google.charts.Line(document.getElementById('chart_div'));\n"
html += 'chart.draw(data, google.charts.Line.convertOptions(options))\n;'
html += '}\n</script>\n'
html += '<body>\n<div id="chart_div" style="width: 900px; height: 500px"></div>\n'
html += '</body>\n</html>'
 
f.write(html)
f.close()

os.system('/usr/lib/chromium-browser/chromium-browser-v7 index.html')










