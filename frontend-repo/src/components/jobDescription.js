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
    const jobOverviewItem = "How You'll Make An Impact";
    const jobOverViewListArray = [
      "Design, develop, and maintain scalable and high-performance backend systems utilizing distributed event driven service architecture.",
      "Configure and manage message buses for efficient communication between distributed systems and services.",
      "Expand and optimize existing access management and authentication systems to accommodate custom authorization flows and integrate with third party identity providers.",
      "Evolve existing deployment pipelines to increase time to market capabilities.",
      "Ensure the adoption and evolution of organizational security policies.",
      "Implement appropriate code and system testing strategies.",
      "Track and monitor progress through typical Agile processes.",
      "Conduct code reviews, mentor junior developers, and contribute to a culture of continuous improvement.",
      "Troubleshoot and resolve complex issues in collaboration withn operations and support teams.",
      "Collaborate with product partners to provide technical prospective and realistic estimates in establishing team roadmaps.",
      "Provide daily focus on security best practices to ensure data and code protections.",
    ];
    const aboutTheOrgItem = "Welcome To Bushel's Corner of the Internet";
    const aboutTheOrgArray = [
      "Why does Bushel exist? To ensure humanity and our planet have a secure and healthy future. Bushel believes agriculture is the most important industry on the planet. Agriculture’s physical infrastructure could be considered the greatest advancement in the grain industry in the last century. We believe the agriculture industry needs to build a complementary digital infrastructure - that’s where Bushel comes in.",
      "Bushel builds software for the grain industry. Our mission is to connect the Grain Industry through digital infrastructure.",
      "Today, we have the largest network of elevators and growers, connecting the most extensive data set in the industry. How have we done that? By offering real value to growers and grain companies through a digital set of tools.",
      "Bushel is headquartered in Fargo, ND - one of the best places to live if you ask us! This position is remote eligible. See below for the list of eligible states.",
    ];

    const jobRequirementsItem = "What Bushel Is Looking For";
    const jobRequirementsArray = [
      "Bachelor’s or Master’s degree in Computer Science or related field.",
      "7+ years of proven experience as a Senior Software Engineer with a focus on backend systems.",
      "Experience designing and implementing microservice architecture and associated best practices.",
      "Understanding of event driven design strategies.",
      "In-depth knowledge of message buses (e.g., Apache Pulsar, RabbitMQ) and experience in implementing and managing distributed messaging systems.",
      "Familiarity with API development and scalability.",
      "Expertise in developing and optimizing identity services, including authentication and authorization mechanisms.",
      "Proficient in various programming languages with an emphasis on Java/Kotlin.",
      "Experience with containerization technologies including Kubernetes.",
      "Solid understanding of software development best practices, version control, and CI/CD pipelines.",
      "Experience and knowledge of relational and noSQL database design and implementations.",
      "Ability to implement performant data querying techniques.",
      "Versed in various quality assurance strategies including system, functional, and unit testing.",
      "Strong understanding of security best practices around access and exposure.",
      "Effective problem solving skills, with the ability to analyze complex issues and provide effective solutions.",
      "Excellent communication and collaboration skills.",
    ];
    const jobResponsibilitiesItem = "How You'll Make An Impact";
    const jobResponsibilitiesArray = [
      "Design, develop, and maintain scalable and high-performance backend systems utilizing distributed event driven service architecture.",
      "Configure and manage message buses for efficient communication between distributed systems and services.",
      "Expand and optimize existing access management and authentication systems to accommodate custom authorization flows and integrate with third party identity providers.",
      "Evolve existing deployment pipelines to increase time to market capabilities.",
      "Ensure the adoption and evolution of organizational security policies.",
      "Implement appropriate code and system testing strategies.",
      "Track and monitor progress through typical Agile processes.",
      "Conduct code reviews, mentor junior developers, and contribute to a culture of continuous improvement.",
      "Troubleshoot and resolve complex issues in collaboration with operations and support teams.",
      "Collaborate with product partners to provide technical prospective and realistic estimates in establishing team roadmaps.",
      "Provide daily focus on security best practices to ensure data and code protections.",
    ];
    const compensationItem = "Bushel Benefits";
    const compensationArray = [
      "$115,000.00 - $140,000.00 Salary/year",
      "Optional Work from Home",
      "Competitive BCBS Health Insurance with contribution to premium",
      "Health Savings Account (HSA) with matching dollars",
      "Flexible Spending Accounts",
      "Dental and Vision Insurance",
      "Hybrid work environment | Flexible working hours | Work-life balance",
      "Basic Life Insurance and Short-Term Disability paid by Bushel",
      "Additional Voluntary Life Insurance options and Long-Term Disability",
      "Voluntary Accident Insurance and Critical Illness Insurance",
      "Flexible (Unlimited) Paid Time Off, 9 Paid Holidays, and 1 Volunteer Day",
      "Up to 12 weeks of Paid Parental Leave, including foster care and adoption",
      "401(k) Retirement with 4% company match with immediate vesting",
      "Employee Assistance Program and BetterHelp counseling services",
      "Learning and development and internal mentorship opportunities",
    ];
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
