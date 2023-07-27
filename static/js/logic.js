// Function to create the chart using Chart.js
function createChart(data) {
  const years = [];
  const maleAttacks = [];
  const femaleAttacks = [];
  const DATA_COUNT = 12;
  const NUMBER_CFG = { count: DATA_COUNT, min: 0, max: 110 };

  data.forEach((item) => {
    years.push(item._id.Year);
    if (item._id.Sex === "M") {
      maleAttacks.push(item.count);
      femaleAttacks.push(null);
    } else {
      maleAttacks.push(null);
      femaleAttacks.push(item.count);
    }
  });

  const ctx = document.getElementById("myChart").getContext("2d");
  const myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: years,
      datasets: [
        {
          label: "Male Attacks",
          data: maleAttacks,
          backgroundColor: "rgb(75, 192, 192, 0.5)",
          borderColor: "rgba(75, 192, 192)",
          borderWidth: 2,
          borderRadius: 5,
          borderSkipped: false,
        },
        {
          label: "Female Attacks",
          data: femaleAttacks,
          backgroundColor: "rgba(255, 99, 132, 0.5)",
          borderColor: "rgba(255, 99, 132, 1)",
          borderWidth: 2,
          borderRadius: 5,
          borderSkipped: false,
        },
      ],
    },
    options: {
      responsive: true,
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
