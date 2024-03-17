//import './jobDescription.css';
import React from "react";
import { Worker, Viewer } from "@react-pdf-viewer/core";
import "@react-pdf-viewer/core/lib/styles/index.css";
import styled from "styled-components";

const PDFContainer = styled.div`
  padding: 20px;
  border: 10px solid #57c4e1;
  margin: 10px;
  border-radius: 10px;
  background-color: white;
`;

const jobDescription = () => {
  const pdfUrl = "/pdf/SFSoftwareDeveloper.pdf";
  return (
    <div>
      <h2 style={{ color: "white" }}>Job Description</h2>
      <PDFContainer className="scrollable">
        <Worker workerUrl="https://unpkg.com/pdfjs-dist@3.4.120/build/pdf.worker.min.js">
          <Viewer fileUrl={pdfUrl} />
        </Worker>
      </PDFContainer>
    </div>
  );
};

export default jobDescription;
