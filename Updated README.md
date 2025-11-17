# CDSCO SEC RSS Feed

Automated RSS feed for CDSCO Subject Expert Committee (SEC) notifications and drug approval updates.

## RSS Feed URL

Subscribe to the feed here:
[**https://simpleman181.github.io/cdsco-sec-rss-feed/feed.xml**](https://simpleman181.github.io/cdsco-sec-rss-feed/feed.xml)

## What This Feed Provides

This RSS feed automatically monitors the [CDSCO SEC page](https://cdsco.gov.in/opencms/opencms/en/Committees/SEC/) and provides updates for:
- SEC meeting recommendations
- Drug approval decisions
- Committee minutes
- Regulatory notifications

## Categories Covered

- SEC Pulmonary
- SEC Radio-Diagnostic  
- SEC Endocrinology & Metabolism
- SEC Cardiovascular
- SEC Oncology and Hematology
- SEC Vaccine Section
- SEC Analgesics & Other categories

## How It Works

1. **Scraper** (`scraper.py`) - Fetches latest notifications from CDSCO SEC page
2. **RSS Generator** (`generate_rss.py`) - Converts data to RSS XML format
3. **GitHub Actions** - Runs automatically daily at 9 AM IST
4. **GitHub Pages** - Hosts the RSS feed publicly

## Manual Update

You can manually trigger an update by going to the [Actions tab](../../actions) and running the "Update RSS Feed" workflow.

## Local Development

