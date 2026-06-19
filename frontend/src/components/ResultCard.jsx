function ResultCard(props) {
  return (
    <div className="result-card">

      <h2>Result</h2>

      {
        props.prediction === "Fake" ? (
          <h3>🔴 Fake</h3>
        ) : props.prediction === "Real" ? (
          <h3>🟢 Real</h3>
        ) : (
          <h3>No Result</h3>
        )
      }

      <p>
        Confidence: {props.confidence}%
      </p>

      <div className="progress-bar">

        <div
          className="progress-fill"
          style={{
            width: `${props.confidence}%`
          }}
        ></div>

      </div>

    </div>
  );
}

export default ResultCard;