# Postmortem: Noble Perfumes E-commerce Outage

## Issue Summary

- **Duration:**
  - Start Time: February 17, 2024, 14:00 GMT.
  - End Time: February 17, 2024, 17:30 GMT.

- **Impact:**
  - The checkout and order processing service experienced a 3.5-hour outage.
  - Users reported inability to complete purchases, affecting approximately 20% of our user base.

- **Root Cause:**
  - Improper configuration of MySQL master-slave replication, leading to write failures.

## Timeline

- **Detection:**
  - Detected at 14:00 GMT through monitoring alerts indicating increased transaction failures.

- **Actions Taken:**
  - Investigated frontend and backend services, initially suspected network issues.
  - Assumed a load-related problem and increased server capacity.
  - Realized the issue was database-related; focused on read operations due to misleading signals.

- **Misleading Paths:**
  - Initial investigation prioritized frontend issues, delaying identification of the database misconfiguration.
  - Assumed network latency due to increased traffic, diverting attention from the core problem.

- **Escalation:**
  - Escalated to Yandah, our database engineer at 15:30 GMT when database logs revealed anomalies.

- **Resolution:**
  - Corrected MySQL master-slave replication configuration at 17:00 GMT.
  - Deployed a puppet script to reconcile and update inconsistent data resulting from the write failures.

## Root Cause and Resolution

- **Root Cause:**
  - The misconfiguration in MySQL master-slave replication caused writes to fail, disrupting the order processing flow.

- **Resolution:**
  - Configured MySQL master-slave replication correctly by pointing to the correct hostname to ensure write operations were replicated successfully.

## Corrective and Preventative Measures

- **Improvements/Fixes:**
  - Enhance monitoring systems and unit tests to detect both read and write anomalies.

- **Tasks to Address the Issue:**
  - Implement automated checks for write operations integrity and alert mechanisms.

## Conclusion

The Noble Perfumes E-commerce outage on February 17, 2024, was a result of misconfigured MySQL master-slave replication, impacting the checkout and order processing service for approximately 20% of users. The incident detection was delayed due to initial misdirection in investigations, focusing on frontend and network issues. Escalation to the database engineering team and subsequent correction of the replication configuration restored normal service by 17:30 GMT.

To prevent future occurrences, we commit to conducting regular configuration audits, enhancing monitoring capabilities, and implementing automated checks for write operations. Training sessions for the operations team will also be scheduled to improve incident response and debugging skills.

---

## Postmortem Advanced

# Postmortem: When the Database Took a Coffee Break

![Hilarious Sql Jokes](https://yellowjokes.com/assets/img/jokes/8520.jpg)

## What Happened?

- At about 14:00 GMT, February 17th, 2024, until 3.5 hours later, our checkout and order processing service decided to take a break affecting about 20% of our users.
- The issue was that our database was not properly configured for MySQL master-slave replication, leading to write failures.

## The Rebellious Streak

- After our monitoring systems started screaming and popping up all the red flags, we investigated frontend and backend services, feeling like detectives in a mystery novel.
- Initially, we thought this was a load problem; we were wrong. The issue was database-related, and we missed it because all our read operations were fine.

## What Caused the Wild-goose Chase

- We blamed network latency for the chaos, diverting our attention from the real mischief-maker.

## What Then After?

- We sounded the alarm to our database engineer, Yandah, at 15:30 GMT after we finally found the real culprit.
- She performed her magical puppet scripts and finally fixed the MySQL master-slave replication issue at 17:00 GMT.

## The Root Cause of All This Mess

- The misconfigured database played us, refusing to replicate writes properly and disrupting the order processing party.

## How We Fixed It

- Reconfiguration of MySQL master-slave replication did the trick. We made sure it plays well with others by telling them who the real host was.

## Our Plans to Stop This Chaos Again in the Future

- We upgraded our monitoring systems to detect hiccups in both read and write, making our systems more vigilant.
- We conducted a thorough review of all database configurations, ensuring that the database is well-behaved.

## To Wrap Up

This postmortem not only highlights the technical nitty-gritty but also brings a touch of humor to our journey of chasing down gremlins in the digital world. Stay tuned for more adventures, because in the world of Noble Perfumes, even our databases take coffee breaks.
