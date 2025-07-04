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
            height: 300,
            width: 500,
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
                fontSize: '11px',
                colors: ["#black"]
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
                fontSize: '14px',
                fontWeight: 'bold',
                color: '#444'
            }
        }
    };

    var chart = new ApexCharts(document.querySelector("#top10dividendos"), options);
    chart.render();
}

async function graficoPvp() {
    const dados = await fetchMaioresDividendos();

    const acoes = dados.map(item => item.codigo);
    const pvp = dados.map(item => item.p_vp);

    function gerarNumeroAleatorio(tamanho) {
        return Math.floor(Math.random() * tamanho);
    }

    function getCor(valor) {
        if (valor > 4) 
            return '#e61919'
        else if (valor > 2) 
            return '#e5e619';
        return '#0d730d';
    }

    let chart; // manter referência global para destruir depois
    let tamanho = pvp.length;

    function criarGrafico() {
        const numeroAleatorio = gerarNumeroAleatorio(tamanho);
        const valorEscolhido = pvp[numeroAleatorio];
        const acaoEscolhida = acoes[numeroAleatorio];
        const corLabel = getCor(valorEscolhido);

        console.log("Número aleatório atualizado:", numeroAleatorio);
        console.log("Valor escolhido:", valorEscolhido);
        console.log("Ação escolhida:", acaoEscolhida);

        const options = {
            series: [valorEscolhido],
            chart: {
                height: 350,
                type: 'radialBar',
            },
            colors: [corLabel],
            title: {
                text: `P/VP`,
                align: 'center',
                style: {
                    fontSize: '16px',
                    fontWeight: 'bold'
                }
            },
            plotOptions: {
                radialBar: {
                    hollow: {
                        size: '70%',
                    },
                    dataLabels: {
                        name: {
                            show: true,
                            fontSize: '16px'
                        },
                        value: {
                            formatter: function (val) {
                                return val.toFixed(2);
                            }
                        }
                    }
                },
            },
            labels: [acaoEscolhida],
        };

        // Destroi gráfico anterior, se existir
        if (chart) {
            chart.destroy();
        }

        chart = new ApexCharts(document.querySelector("#pvp"), options);
        chart.render();
    }

    criarGrafico(); // cria o gráfico inicialmente
    setInterval(criarGrafico, 4000); // recria a cada 4 segundos
}





async function fetchTop10Lucros() {
    const response = await fetch('http://127.0.0.1:8000/api/top10-maiores-lucros/');
    const data = await response.json();
    return data;
}

async function graficoTop10Lucros() {
    const dados = await fetchTop10Lucros();

    const acoes = dados.map(item => item.codigo);
    const lucros = dados.map(item => item.lucro);

    var options = {
        title: {
            text: `Top 10 Ações que mais lucraram (${hoje})`,
            align: 'center',
            style: {
                fontSize: '14px',
                fontWeight: 'bold',
                color: '#444'
            }
        },
        series: [{
            name: 'Lucro',
            data: lucros
        }],
        chart: {
            type: 'bar',
            height: 300,
            width: 500,
        },
        plotOptions: {
            bar: {
                borderRadius: 4,
                borderRadiusApplication: 'end',
                horizontal: true,
                dataLabels: {
                    position: 'inside' // ✅ Mostra o valor dentro da barra
                }
            }
        },
        dataLabels: {
            enabled: true,
            formatter: function (val) {
                return 'R$ ' + val.toLocaleString('pt-BR');
            },
            style: {
                fontSize: '11px',
                colors: ['#black'] 
            }
        },
        xaxis: {
            categories: acoes,
            labels: {
                formatter: function (val) {
                    return 'R$ ' + val.toLocaleString('pt-BR');
                }
            }
        },
        tooltip: {
            y: {
                formatter: function (val) {
                    return 'R$ ' + val.toLocaleString('pt-BR');
                }
            }
        }
    };

    const chart = new ApexCharts(document.querySelector("#top10lucros"), options);
    chart.render();
}

async function fetchMaioresDividendos() {
    const response = await fetch('http://127.0.0.1:8000/api/maiores-dividendos/');
    const data = await response.json();
    return data;
}

async function graficoMaiorVariacaoDividendos() {
    const dados = await fetchMaioresDividendos();
    console.log("maiores dividendos: ", dados);

    // Agrupa os dividendos por código
    const agrupadoPorCodigo = {};
    dados.forEach(item => {
        if (!agrupadoPorCodigo[item.codigo]) {
            agrupadoPorCodigo[item.codigo] = [];
        }
        agrupadoPorCodigo[item.codigo].push({ x: item.data, y: item.dividendo_atual });
    });

    // Calcula a variação para cada ação
    const variacoes = Object.entries(agrupadoPorCodigo).map(([codigo, valores]) => {
        const dividendos = valores.map(v => v.y);
        const max = Math.max(...dividendos);
        const min = Math.min(...dividendos);
        return { codigo, variacao: max - min };
    });

    // Pega os 5 com maior variação
    const top5 = variacoes
        .sort((a, b) => b.variacao - a.variacao)
        .slice(0, 5)
        .map(item => item.codigo);

    // Filtra os dados apenas com os top 5
    const dadosFiltrados = {};
    top5.forEach(codigo => {
        dadosFiltrados[codigo] = agrupadoPorCodigo[codigo]
            .sort((a, b) => new Date(a.x) - new Date(b.x));
    });

    // Converte para o formato do ApexCharts
    const series = top5.map(codigo => ({
        name: codigo,
        data: dadosFiltrados[codigo]
    }));

    const options = {
        chart: {
            type: 'line',
            height: 400
        },
        title: {
            text: 'Top 5 Ações com Maior Variação de Dividendos',
            align: 'center'
        },
        xaxis: {
            type: 'category',
            title: { text: 'Data' }
        },
        yaxis: {
            title: { text: 'Dividendo Atual' }
        },
        series: series
    };

    const chart = new ApexCharts(document.querySelector("#variacaoDeDividendos"), options);
    chart.render();
}

async function fetchMaioresLucros() {
    const response = await fetch('http://127.0.0.1:8000/api/maiores-lucros/');
    const data = await response.json();
    return data;
}

async function graficoMaiorVariacaoLucros() {
    const dados = await fetchMaioresLucros();
    console.log("maiores Lucros: ", dados);

    // Agrupa os dividendos por código
    const agrupadoPorCodigo = {};
    dados.forEach(item => {
        if (!agrupadoPorCodigo[item.codigo]) {
            agrupadoPorCodigo[item.codigo] = [];
        }
        agrupadoPorCodigo[item.codigo].push({ x: item.data, y: item.lucro });
    });

    // Calcula a variação para cada ação
    const variacoes = Object.entries(agrupadoPorCodigo).map(([codigo, valores]) => {
        const dividendos = valores.map(v => v.y);
        const max = Math.max(...dividendos);
        const min = Math.min(...dividendos);
        return { codigo, variacao: max - min };
    });

    // Pega os 5 com maior variação
    const top5 = variacoes
        .sort((a, b) => b.variacao - a.variacao)
        .slice(0, 5)
        .map(item => item.codigo);

    // Filtra os dados apenas com os top 5
    const dadosFiltrados = {};
    top5.forEach(codigo => {
        dadosFiltrados[codigo] = agrupadoPorCodigo[codigo]
            .sort((a, b) => new Date(a.x) - new Date(b.x));
    });

    // Converte para o formato do ApexCharts
    const series = top5.map(codigo => ({
        name: codigo,
        data: dadosFiltrados[codigo]
    }));

    const options = {
        chart: {
            type: 'line',
            height: 400
        },
        title: {
            text: 'Top 5 Ações com Maior Variação de Lucros',
            align: 'center'
        },
        xaxis: {
            type: 'category',
            title: { text: 'Data' }
        },
        yaxis: {
            title: { text: 'Lucro' }
        },
        series: series
    };

    const chart = new ApexCharts(document.querySelector("#variacaoDeLucros"), options);
    chart.render();

}


document.addEventListener("DOMContentLoaded", function () {
    graficoTop10Dividendos();
    graficoTop10Lucros();
    graficoMaiorVariacaoDividendos();
    graficoMaiorVariacaoLucros();
    graficoPvp()
});


