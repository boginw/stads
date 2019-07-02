# STADS
Toolcase for AAU's STADS system

## Tools

Below is the list of tools this repository provides.

### stads_printer

Loggs into STADS, gets your grades, and prints them in markdown table format. Additionally, it calculates your weighted average.

### stads_scrape

Does the same as stads_printer, but continuesly watching for changes. If stads_scrape detects a change in the list of grades, it will send an email to you, with the printout of stads_printer.

## Configuration

Take a look at the `.env.example` in this repository. You'll need to copy this file, such that you have a new file called `.env`. In this new file, you must type in the appropriate information.

* For `stads_printer`: STADS_USER, STADS_PASS
* For `stads_scrape`: All variables

### AWS

In order to get stads_scrape to send you an email, you'll need to provide programmatic credentials to an AWS account with the following permissions:

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