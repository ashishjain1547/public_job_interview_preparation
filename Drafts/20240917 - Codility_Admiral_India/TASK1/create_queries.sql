CREATE TABLE IF NOT EXISTS GeoData (
    ZipCode REAL,
    ZIP_AverageHomeValue REAL,
    ZIP_AverageIncome REAL,
    ZIP_Population REAL,
    ZIP_LandArea REAL
);

.mode csv
.import /home/ashish/Desktop/Codility_Admiral_India_2024Sep17/TASK1/GeographicData+-+Data+Science.csv GeoData


CREATE TABLE IF NOT EXISTS PolicyData (
    PolicyID REAL,
    State TEXT,
    CoverageGap TEXT,
    CreditScore REAL,
    Age REAL,
    NumberOfVehicles REAL,
    NewestVehicleAge REAL,
    PriorAccidentCount REAL,
    ZipCode REAL,
    TimeInsured REAL,
    ClaimAmount REAL,
    ClaimFlag REAL
);

.mode csv
.import /home/ashish/Desktop/Codility_Admiral_India_2024Sep17/TASK1/PolicyData+-+Data+science.csv PolicyData


-- Transform the continuous variable ApplicantAge into a categorical variable with roughly equal numbers of policies in each

WRONG:

SELECT
	case
		when Age < 25 then '18-24'
		when Age < 30 then '25-29'
		when Age < 35 then '30-34'
		when Age < 40 then '35-39'
		when Age < 45 then '40-44'
		when Age < 50 then '45-49'
		when Age < 55 then '50-54'
		when Age < 60 then '55-59'
		when Age < 65 then '60-64'
		when Age < 70 then '65-69'
		else '70+'
	end as AgeGroup, count(*) as NumPolicies
FROM PolicyData
WHERE ClaimFlag = 1
GROUP BY AgeGroup;


CORRECT:

SELECT
    NTILE(10) OVER (ORDER BY Age) AS quartile, PolicyID
FROM PolicyData;

SELECT
    avg(geo.ZipCode),
    avg(geo.ZIP_AverageHomeValue),
    avg(geo.ZIP_AverageIncome),
    avg(geo.ZIP_Population),
    avg(geo.ZIP_LandArea),
    pd.ClaimFlag
FROM PolicyData pd
JOIN GeoData geo
    ON pd.ZipCode = geo.ZipCode
GROUP BY pd.ClaimFlag;
