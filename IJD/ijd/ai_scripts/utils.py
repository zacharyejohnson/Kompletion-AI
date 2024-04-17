
import json


def generate_job_description(job_overview_title, job_overview_list, about_the_org_title, about_the_org_list,
                             job_requirements_title, job_requirements_list, job_responsibilities_title,
                             job_responsibilities_list, compensation_title, compensation_list):
    job_description_data = {
        "jobOverviewTitle": job_overview_title,
        "jobOverviewList": job_overview_list,
        "aboutTheOrgTitle": about_the_org_title,
        "aboutTheOrgList": about_the_org_list,
        "jobRequirementsTitle": job_requirements_title,
        "jobRequirementsList": job_requirements_list,
        "jobResponsibilitiesTitle": job_responsibilities_title,
        "jobResponsibilitiesList": job_responsibilities_list,
        "compensationTitle": compensation_title,
        "compensationList": compensation_list
    }

    # Convert the Python dictionary to a JSON string
    return job_description_data


