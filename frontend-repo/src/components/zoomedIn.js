import "../styles/jobDescription.css";
import React from "react";

const ZoomedIn = ({ category, title, list, setZoomedIn }) => {
  const pdfUrl = "/pdf/SFSoftwareDeveloper.pdf";
  return (
    <div>
      <div className="zoomedIn">
        <h1 style={{ textAlign: "center" }}>{category}</h1>
        <h2 style={{ textAlign: "center" }}>{title}</h2>
        <ul>
          {list?.map((item) => {
            return <li key={item}>{item}</li>;
          })}
        </ul>
      </div>
    </div>
  );
};

export default ZoomedIn;
