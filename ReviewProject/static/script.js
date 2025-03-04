function classifyReview() {
    const reviewText = document.getElementById("review").value;

    fetch("/classify/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ review: reviewText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Sentiment: " + data.sentiment;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error processing request.";
    });
}