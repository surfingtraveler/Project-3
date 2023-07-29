// Function to create the chart using Chart.js
function createChart(data) {
  const years = data.map((item) => item._id);
  const maleCounts = data.map((item) => item.male_count);
  const femaleCounts = data.map((item) => item.female_count);
  const ctx = document.getElementById("myChart").getContext("2d");
  const myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: years,
      datasets: [
        {
          label: "Male Attacks",
          data: maleCounts,
          backgroundColor: "rgb(75, 192, 192, 0.5)",
          borderColor: "rgba(75, 192, 192)",
          borderWidth: 2,
          borderRadius: 5,
          borderSkipped: false,
        },
        {
          label: "Female Attacks",
          data: femaleCounts,
          backgroundColor: "rgb(153, 102, 255, 0.5)",
          borderColor: "rgb(153, 102, 255)",
          borderWidth: 2,
          borderRadius: 5,
          borderSkipped: false,
        },
      ],
    },
    options: {
      responsive: true,
      beginAtZero: true,
      plugins: {
        legend: {
          position: "top",
        },
        title: {
          display: true,
          text: "Frequency of Shark Attacks By Sex",
        },
      },
    },
  });
}
// Fetch the data using D3.js
let data = d3
  .json("http://127.0.0.1:5000/shark_attacks_data")
  .then((data) => {
    // Call the createChart function to render the chart
    createChart(data);
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
  });
