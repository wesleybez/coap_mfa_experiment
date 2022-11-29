set grid

set palette model HSV rgbformulae 7,5,15
set style fill solid 0.25

set style data histograms
#set boxwidth 0.7

set terminal pngcairo size 700,524 enhanced font 'Verdana,10'

set datafile separator ","

set xlabel "x - instance number"
set ylabel "y - Time (microseconds)"

set title "CoAP Connection Time"

set output '../reports/coap_time_connection.png'

plot '../datasets/20210514_10_coap_publish_proposta.csv' using 3:xtic(1) title "mfa", \
     '../datasets/20210514_10_coap_publish_autenticated.csv' using 3:xtic(1) title "autenticated", \
     '../datasets/20210514_10_coap_publish_non_auth.csv' using 3:xtic(1) title "non autenticated"

set title "CoAP Publish Time"
set output '../reports/coap_time_publish.png'

plot '../datasets/20210514_10_coap_publish_proposta.csv' using 4:xtic(1) title "mfa", \
     '../datasets/20210514_10_coap_publish_autenticated.csv' using 4:xtic(1) title "autenticated", \
     '../datasets/20210514_10_coap_publish_non_auth.csv' using 4:xtic(1) title "non autenticated"

     
set xlabel "x - Metrics"
set ylabel "y - Time (microseconds)"

set title "CoAP Connection Time Statistics"
set output '../reports/coap_connection_time_statistic.png'

plot './media_tempo.csv' using 2:xtic(1) title "mean", \
	 './maior_tempo.csv' using 2:xtic(1) title "max", \
     './menor_tempo.csv' using 2:xtic(1) title "minor"
     
     
set xlabel "x - Metrics"
set ylabel "y - Time (microseconds)"

set title "CoAP Connection Time MFA Statistics"
set output '../reports/coap_connection_mfa_statistic.png'

plot './mfa_tempo.csv' using 2:xtic(1) title "mean", \
     './mfa_tempo.csv' using 4:xtic(1) title "max", \
     './mfa_tempo.csv' using 6:xtic(1) title "minor"
     
set title "CoAP Publish Time MFA Statistics"
set output '../reports/coap_publish_mfa_statistic.png'

plot './mfa_tempo.csv' using 3:xtic(1) title "mean", \
     './mfa_tempo.csv' using 5:xtic(1) title "max", \
     './mfa_tempo.csv' using 7:xtic(1) title "minor"

     
set xlabel "x - Metrics"
set ylabel "y - Time (microseconds)"

set title "CoAP Publish Time Statistics"
set output '../reports/coap_publish_time_statistic.png'

plot './media_tempo.csv' using 3:xtic(1) title "mean",\
	 './maior_tempo.csv' using 3:xtic(1) title "max", \
     './menor_tempo.csv' using 3:xtic(1) title "minor"
     
     

################################
#     memory charts
################################

set xlabel "x - Instance Number"
set ylabel "y - Memory (KBytes)"

set title "CoAP Memory Consumption"
set output '../reports/coap_memory_publish.png'

plot '../datasets/20210514_10_coap_memory_proposta.csv' using 2:xtic(1) title "mfa", \
     '../datasets/20210514_10_coap_memory_autenticated.csv' using 2:xtic(1) title "autenticated", \
     '../datasets/20210514_10_coap_memory_non_auth.csv' using 2:xtic(1) title "non autenticated"    
     


set xlabel "x - Metrics"
set ylabel "y - Memory (KBytes)"

set title "CoAP Memory Statistics"
set output '../reports/coap_memory_statistic.png'

plot './media_memoria.csv' using 2:xtic(1) title "mean",\
	 './maior_memoria.csv' using 2:xtic(1) title "max", \
     './menor_memoria.csv' using 2:xtic(1) title "minor"
      
     

set xlabel "x - Metrics"
set ylabel "y - Memory (KBytes)"

set title "CoAP Memory MFA Statistics"
set output '../reports/coap_memory_mfa_statistic.png'

plot './mfa_memoria.csv' using 2:xtic(1) title "mean", \
     './mfa_memoria.csv' using 3:xtic(1) title "max", \
     './mfa_memoria.csv' using 4:xtic(1) title "minor" 
     
     #""  using 0:($2+.1):(sprintf("%3.2f",$2)) with labels
     
#     ************ boxplot

set style fill solid 0.25 border -1
set style boxplot outliers pointtype 7
set style data boxplot
set output '../reports/coap_memory_mfa_statistic_boxplot.png'

set title 'My Plot' font 'Arial,14';
#set xtics ('1.0' 1, '1.2' 2, '1.4' 3)
plot '../datasets/20210514_10_coap_memory_proposta.csv' using (0):2 title "mfa_r", \
     '../datasets/20210514_10_coap_memory_autenticated.csv' using (1.0):2 title "autenticated", \
     '../datasets/20210514_10_coap_memory_non_auth.csv' using (2.0):2 title "non autenticated"  
     