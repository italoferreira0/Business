const hoje = new Date().toLocaleDateString('en-CA', {
  timeZone: 'America/Sao_Paulo'
});
async function fetchTop10dividendo() {
    const response = await fetch('http://127.0.0.1:8000/api/top10-dividendos/');
    const data = await response.json();
    return data;
}

async function graficoTop10Dividendos() {
    const dados = await fetchTop10dividendo();

    const acoes = dados.map(item => item.codigo);
    const dividendo_atual = dados.map(item => item.dividendo_atual);

    console.log("Códigos recebidos:", acoes);

    var options = {
        series: [{
            name: 'Dividend Yield',
            data: dividendo_atual
        }],
        chart: {
            height: 350,
            type: 'bar',
        },
        plotOptions: {
            bar: {
                borderRadius: 10,
                dataLabels: {
                    position: 'top', // top, center, bottom
                },
            }
        },
        dataLabels: {
            enabled: true,
            formatter: function (val) {
                return val + "%";
            },
            offsetY: -20,
            style: {
                fontSize: '12px',
                colors: ["#304758"]
            }
        },

        xaxis: {
            categories: acoes,
            //   position: 'top',
            axisBorder: {
                show: false
            },
            axisTicks: {
                show: false
            },
            crosshairs: {
                fill: {
                    type: 'gradient',
                    gradient: {
                        colorFrom: '#D8E3F0',
                        colorTo: '#BED1E6',
                        stops: [0, 100],
                        opacityFrom: 0.4,
                        opacityTo: 0.5,
                    }
                }
            },
            tooltip: {
                enabled: true,
            }
        },
        yaxis: {
            axisBorder: {
                show: false
            },
            axisTicks: {
                show: false,
            },
            labels: {
                show: false,
                formatter: function (val) {
                    return val + "%";
                }
            }

        },
        title: {
            text: `Top 10 Ações que mais pagaram dividendos (${hoje})`,
            align: 'center',
            style: {
                fontSize: '16px',
                fontWeight: 'bold',
                color: '#444'
            }
        }
    };

    var chart = new ApexCharts(document.querySelector("#top10dividendos"), options);
    chart.render();


}

document.addEventListener("DOMContentLoaded", function () {
    graficoTop10Dividendos();
});