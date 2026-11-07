# Security and research-data handling

This repository intentionally contains an **offline demonstrator** with entirely synthetic project records. It does not implement authentication, connect to a database, ingest private user profiles or call paid external services.

## Historical code safety

Related historical coursework repositories may contain insecure configurations, including embedded database credentials and plaintext-password handling. Do **not** copy, deploy or reuse those configurations. If any historic credentials were real, revoke/rotate them at the provider, audit access logs, remove credentials from the provider's configuration and address historical Git revisions through an appropriate repository-history remediation process. Deleting a line in the latest commit is **not** sufficient to erase an exposed secret.

Never add actual student, faculty, company, confidential project or personally identifiable data without permission and a documented lawful basis, security controls and risk review. A public repository must not contain production secrets or original restricted datasets.

## Limitations

The standalone recommender is educational and has not been independently security-tested, evaluated for fairness or assessed for UK GDPR compliance. Do not deploy it as a real matchmaking or admissions system without further work.

To report security concerns, contact the repository owner privately. Do not paste credentials into public issues.
