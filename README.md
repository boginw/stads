# STADS

Toolcase for AAU's STADS system

## Get Started

Make sure you have Python 3 and `pip` installed. I would recommend starting a `virtualenv` ([install guide](https://virtualenv.pypa.io/en/stable/installation.html)). Now, running the next commands will start your virtual environment, and install all the dependencies.

```bash
source bin/activate
pip install -r requirements.txt
```

To exit the environment, simply type `deactivate`. The next section describes the main tools of this library. To run them, simply type `python3 stads_*`, where `*` is the toolname. See the [Configuration](#configuration) section in order to provide the credentials for STADS and AWS.

## Tools

Below is the list of tools this repository provides.

### Printer

Loggs into STADS, gets your grades, and prints them in markdown table format. Additionally, it calculates your weighted average.

### Scrape

Does the same as the printer, but continuesly watching for changes. If Scrape detects a change in the list of grades, it will send an email to you, with the printout of the printer.

## Configuration

Take a look at the `.env.example` in this repository. You'll need to copy this file, such that you have a new file called `.env`. In this new file, you must type in the appropriate information.

* For `stads_printer`: STADS_USER, STADS_PASS
* For `stads_scrape`: All variables

### AWS

In order to get stads_scrape to send you an email, you'll need to provide programmatic credentials to an AWS account with an attached policy with the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ses:SendEmail",
            "Resource": "*"
        }
    ]
}
```