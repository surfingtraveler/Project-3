document.addEventListener("DOMContentLoaded", (event) => {
  d3.json("/api/shark_attacks")
    .then((data) => {
      let ctx = document.getElementById("myCanvas").getContext("2d");
      let labels = data.map((item) => item.Date);
      let dataset = data.map((item) => item.Count);

      new Chart(ctx, {
        type: "bar",
        data: {
          labels: labels,
          datasets: [
            {
              label: "Frequency of Shark Attacks",
              data: dataset,
              backgroundColor: "rgb(153, 102, 255, 0.5)",
              borderColor: "rgb(153, 102, 255)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: "Frequency",
              },
            },
            x: {
              title: {
                display: true,
                text: "Years-Months",
              },
            },
          },
        },
      });
    })
    .catch((error) => console.error(error));
});
