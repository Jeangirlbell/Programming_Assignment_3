import county_demographics
from data import CountyDemographics
import build_data

def population_total(counties: list[CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total+= county.population['2014 Population']
    return total

def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    filtered_counties = []
    for county in counties:
        if county.state == state:
            filtered_counties.append(county)
    return filtered_counties

def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    total=0
    for county in counties:
        if key in county.education:
          percent=county.education[key]
          total+= (percent/100.0) * county.population['2014 Population']
    return total

def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total=0
    for county in counties:
        if key in county.ethnicities:
            percent=county.ethnicities[key]
            total+= (percent/100.0) * county.population['2014 Population']
    return total


def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0.0
    for county in counties:
        percent = county.income['Persons Below Poverty Level']
        total += (percent / 100.0) * county.population['2014 Population']
    return total

def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    total_population=population_total(counties)
    if total_population != 0:
        total_education=population_by_education(counties, key)
        return total_education/total_population * 100.0
    return 0


def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total_population=population_total(counties)
    if total_population != 0:
        total_ethnicity=population_by_ethnicity(counties, key)
        return total_ethnicity/total_population * 100.0
    return 0

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population=population_total(counties)
    if total_population != 0:
        total_ethnicity=population_below_poverty_level(counties)
        return total_ethnicity/total_population * 100.0
    return 0

def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
        result=[]
        for county in counties:
            if key in county.education and county.education[key] > threshold:
                result.append(county)
        return result

def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
        result=[]
        for county in counties:
            if key in county.education and county.education[key] < threshold:
                result.append(county)
        return result

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
        result=[]
        for county in counties:
            if key in county.ethnicities and county.ethnicities[key] > threshold:
                result.append(county)
        return result


def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] < threshold:
            result.append(county)
    return result

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result=[]
    for county in counties:
        if county.income["Persons Below Poverty Level"] > threshold:
            result.append(county)
    return result

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result=[]
    for county in counties:
        if county.income["Persons Below Poverty Level"] < threshold:
            result.append(county)
    return result
