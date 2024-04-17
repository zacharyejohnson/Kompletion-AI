import "../styles/jobDescription.css";
import React, { useState, useEffect } from "react";
import ZoomedIn from "./zoomedIn";
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

const JobDescription = ({ setSuggestedQuestions, setCategory }) => {
  const [jobOverViewTitle, setJobOverViewTitle] = useState("");
  const [jobOverViewList, setJobOverViewList] = useState([]);
  const [aboutTheOrgTitle, setAboutTheOrgTitle] = useState("");
  const [aboutTheOrgList, setAboutTheOrgList] = useState([]);
  const [jobRequirementsTitle, setJobRequirementsTitle] = useState("");
  const [jobRequirementsList, setJobRequirementsList] = useState([]);
  const [jobResponsibilitiesTitle, setJobResponsibilitiesTitle] = useState("");
  const [jobResponsibilitiesList, setJobResponsibilitiesList] = useState([]);
  const [compensationTitle, setCompensationTitle] = useState("");
  const [compensationList, setCompensationList] = useState([]);
  const [zoomedIn, setZoomedIn] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState("");
  const [selectedTitle, setSelectedTitle] = useState("");
  const [selectedList, setSelectedList] = useState([]);

  useEffect(() => {
    const jobOverviewItem = "";
    const jobOverViewListArray = [];
    const aboutTheOrgItem = "";
    const aboutTheOrgArray = [];

    const jobRequirementsItem = "";
    const jobRequirementsArray = [];
    const jobResponsibilitiesItem = "";
    const jobResponsibilitiesArray = [];
    const compensationItem = "";
    const compensationArray = [];
    setJobOverViewTitle(jobOverviewItem);
    setJobOverViewList(jobOverViewListArray);
    setAboutTheOrgTitle(aboutTheOrgItem);
    setAboutTheOrgList(aboutTheOrgArray);
    setJobRequirementsTitle(jobRequirementsItem);
    setJobRequirementsList(jobRequirementsArray);
    setJobResponsibilitiesTitle(jobResponsibilitiesItem);
    setJobResponsibilitiesList(jobResponsibilitiesArray);
    setCompensationTitle(compensationItem);
    setCompensationList(compensationArray);
  }, []);

  useEffect(() => {
    if (!zoomedIn) {
      setCategory("Home");
      setSelectedCategory("");
      setSelectedTitle("");
      setSelectedList([]);
      setSuggestedQuestions([]);
    }
  }, [zoomedIn]);

  const zoomInFunction = (zoomed, category, title, list, questions) => {
    setZoomedIn(zoomed);
    setCategory(category);
    setSelectedTitle(title);
    setSelectedList(list);
    setSuggestedQuestions(questions);
  };

  const pdfUrl = "/pdf/SFSoftwareDeveloper.pdf";
  return (
    <>
      {zoomedIn && (
        <div
          style={{ position: "absolute", top: 0 }}
          className="backBtn"
          onClick={() => setZoomedIn(false)}>
          <p>Back</p>
        </div>
      )}
      <div className="btnList">
        <div style={{ width: "100%", textAlign: "center" }}>
          <div
            className="btn"
            onClick={() =>
              zoomInFunction(
                true,
                "Job Overview",
                jobOverViewTitle,
                jobOverViewList,
                [
                  "Is this a leadership role?",
                  "Will I be maintaining existing projects or building new ones?",
                  "how much of this job involves coding?",
                ]
              )
            }>
            Job Overview
          </div>
          <div className="btn" onClick={() => setZoomedIn(false)}>
            JD Home
          </div>
          <div
            className="btn"
            onClick={() =>
              zoomInFunction(
                true,
                "About the Organization",
                aboutTheOrgTitle,
                aboutTheOrgList,
                [
                  "When was this company established?",
                  "Do you primarly work with only one product?",
                  "Can you list me some of your core values?",
                ]
              )
            }>
            About Org
          </div>
          <div
            className="btn"
            onClick={() =>
              zoomInFunction(
                true,
                "Job Requirements",
                jobRequirementsTitle,
                jobRequirementsList,
                [
                  "Can years of experience offset not having a degree?",
                  "What requirements do you place more value in and how much of this is a wish list?",
                  "What does 'proven experience' mean?",
                ]
              )
            }>
            Qualifications
          </div>
          <div
            className="btn"
            onClick={() =>
              zoomInFunction(
                true,
                "Job Responsibilities",
                jobResponsibilitiesTitle,
                jobResponsibilitiesList,
                [
                  "Is this a leadership role?",
                  "does 'resolving complex issues' mainly involve fixing bugs or is it more about adding complex features?",
                  "You mentioned product partners? Will I be face to face with clients and customers?",
                ]
              )
            }>
            Responsibilities
          </div>
          <div
            className="btn"
            onClick={() =>
              zoomInFunction(
                true,
                "Compensation/Benefits",
                compensationTitle,
                compensationList,
                [
                  "Can you define 'unlimited PTO' and does it require approval?",
                  "Can you expand on 'learning and development' as a benefit, what do you actually offer in this area?",
                  "Is the life and disability insurance fully covered or only partially covered?",
                ]
              )
            }>
            Compensation/Benefits
          </div>
        </div>
      </div>
      {zoomedIn ? (
        <ZoomedIn
          category={selectedCategory}
          title={selectedTitle}
          list={selectedList}
          setZoomedIn={setZoomedIn}
        />
      ) : (
        <div>
          <div
            onClick={() =>
              zoomInFunction(
                true,
                "Job Overview",
                jobOverViewTitle,
                jobOverViewList,
                [
                  "Is this a leadership role?",
                  "Will I be maintaining existing projects or building new ones?",
                  "how much of this job involves coding?",
                ]
              )
            }
            className="category">
            <h1 style={{ textAlign: "center" }}>Job Overview</h1>
            <h2 style={{ textAlign: "center" }}>{jobOverViewTitle}</h2>
            <ul>
              {jobOverViewList?.map((jobOverViewListItem) => {
                return <li key={jobOverViewListItem}>{jobOverViewListItem}</li>;
              })}
            </ul>
          </div>
          <div
            onClick={() =>
              zoomInFunction(
                true,
                "About the Organization",
                aboutTheOrgTitle,
                aboutTheOrgList,
                [
                  "When was this company established?",
                  "Do you primarly work with only one product?",
                  "Can you list me some of your core values?",
                ]
              )
            }
            className="category">
            <h1 style={{ textAlign: "center" }}>About the Organization</h1>
            <h2 style={{ textAlign: "center" }}>{aboutTheOrgTitle}</h2>
            <ul>
              {aboutTheOrgList?.map((aboutTheOrgListItem) => {
                return <li key={aboutTheOrgListItem}>{aboutTheOrgListItem}</li>;
              })}
            </ul>
          </div>
          <div
            onClick={() =>
              zoomInFunction(
                true,
                "Job Requirements",
                jobRequirementsTitle,
                jobRequirementsList,
                [
                  "Can years of experience offset not having a degree?",
                  "What requirements do you place more value in and how much of this is a wish list?",
                  "What does 'proven experience' mean?",
                ]
              )
            }
            className="category">
            <h1 style={{ textAlign: "center" }}>Job Requirements</h1>
            <h2 style={{ textAlign: "center" }}>{jobRequirementsTitle}</h2>
            <ul>
              {jobRequirementsList?.map((jobRequirementsListItem) => {
                return (
                  <li key={jobRequirementsListItem}>
                    {jobRequirementsListItem}
                  </li>
                );
              })}
            </ul>
          </div>
          <div
            onClick={() =>
              zoomInFunction(
                true,
                "Job Responsibilities",
                jobResponsibilitiesTitle,
                jobResponsibilitiesList,
                [
                  "Is this a leadership role?",
                  "does 'resolving complex issues' mainly involve fixing bugs or is it more about adding complex features?",
                  "You mentioned product partners? Will I be face to face with clients and customers?",
                ]
              )
            }
            className="category">
            <h2 style={{ textAlign: "center" }}>{jobResponsibilitiesTitle}</h2>
            <ul>
              {jobResponsibilitiesList?.map((jobResponsibilitiesListItem) => {
                return (
                  <li key={jobResponsibilitiesListItem}>
                    {jobResponsibilitiesListItem}
                  </li>
                );
              })}
            </ul>
          </div>
          <div
            onClick={() =>
              zoomInFunction(
                true,
                "Compensation/Benefits",
                compensationTitle,
                compensationList,
                [
                  "Can you define 'unlimited PTO' and does it require approval?",
                  "Can you expand on 'learning and development' as a benefit, what do you actually offer in this area?",
                  "Is the life and disability insurance fully covered or only partially covered?",
                ]
              )
            }
            className="category">
            <h1 style={{ textAlign: "center" }}>Compensation/Benefits</h1>
            <h2 style={{ textAlign: "center" }}>{compensationTitle}</h2>
            <ul>
              {compensationList?.map((compensationListItem) => {
                return (
                  <li key={compensationListItem}>{compensationListItem}</li>
                );
              })}
            </ul>
          </div>

          {/* <PDFContainer className="scrollable">
        <Worker workerUrl="https://unpkg.com/pdfjs-dist@3.4.120/build/pdf.worker.min.js">
          <Viewer fileUrl={pdfUrl} />
        </Worker>
      </PDFContainer> */}
        </div>
      )}
      ;
    </>
  );
};

export default JobDescription;
