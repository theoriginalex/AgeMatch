window.addEventListener('load', function() {
    try {
        // Obtener el canvas
        const ctx = document.getElementById('grafico-emociones').getContext('2d');
        
        // Verificar datos
        const rawData = document.getElementById('grafico-emociones').dataset.registros;
        if (!rawData) {
            console.error('No hay datos en el contenedor');
            return;
        }

        // Parsear datos
        const registros = JSON.parse(rawData);
        if (!registros || registros.length === 0) {
            console.error('No hay registros válidos');
            return;
        }

        // Preparar datos para el gráfico
        const labels = registros.map(r => r.emocion);
        const data = registros.map(r => r.total);

        // Configurar el gráfico
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: [
                        '#FF6384',
                        '#36A2EB',
                        '#FFCE56',
                        '#4BC0C0',
                        '#9966FF',
                        '#FF9F40'
                    ],
                    borderWidth: 2,
                    borderColor: '#fff',
                    borderRadius: 10
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'left',
                        labels: {
                            color: '#fff',
                            font: {
                                size: 14
                            }
                        }
                    }
                }
            }
        });

    } catch (error) {
        console.error('Error al crear el gráfico:', error);
    }
});

            // Configuración del gráfico
            const option = {
                backgroundColor: '#1a1a1a',
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c} ({d}%)'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    top: 'center',
                    textStyle: {
                        color: '#fff',
                        fontSize: 14
                    }
                },
                series: [
                    {
                        name: 'Emociones',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: '28',
                                fontWeight: 'bold',
                                color: '#fff'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: seriesData
                    }
                ]
            };

            // Aplicar configuración
            chart.setOption(option);

            // Manejar redimensionamiento
            window.addEventListener('resize', function() {
                chart.resize();
            });

            console.log('Gráfico ECharts creado exitosamente');

        } catch (parseError) {
            console.error('Error al procesar datos:', parseError);
        }

    } catch (error) {
        console.error('Error al crear el gráfico:', error);
    }
});


