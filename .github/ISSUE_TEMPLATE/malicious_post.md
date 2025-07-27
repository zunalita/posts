---
name: 🛑 Malicious or Misleading Post
description: Report a post that contains false information, security risks, or violates guidelines.
title: "Potential Vulnerable Post: [FILENAME].md"
labels: ["malicious-post"]

body:
  - type: markdown
    attributes:
      value: |
        ## ⚠️ Help us keep the content safe!

        Use this form to report posts that may be **inaccurate**, **offensive**, **misleading**, or contain **malicious code**.  
        Reports are reviewed within **72 hours** and actions will be taken accordingly.

  - type: input
    id: file_url
    attributes:
      label: 🔗 Post URL
      description: Paste the full GitHub URL of the affected file (must be inside `/posts`)
      placeholder: https://github.com/zunalita/posts/blob/main/posts/xx-xx-xxxx-malicious.md
    validations:
      required: true

  - type: checkboxes
    id: confirm_read
    attributes:
      label: ✅ Confirmation
      description: Please confirm the following:
      options:
        - label: I’ve reviewed the file and believe it may be harmful, misleading, or in violation of guidelines.
          required: true

  - type: dropdown
    id: issue_type
    attributes:
      label: 🚩 Type of Issue
      description: What kind of problem does this post contain?
      options:
        - Misinformation / Fake content
        - Sensitive or private information
        - Malicious code / security threat
        - Inappropriate or offensive content
        - Other (explain below)
    validations:
      required: true

  - type: textarea
    id: details
    attributes:
      label: 📄 Description of the Problem
      description: Explain the issue clearly. If applicable, mention line numbers or sections.
      placeholder: |
        This post contains malicious JS on line 10 that triggers an automatic download...
        Or: It includes personal data of a user...
    validations:
      required: true

  - type: textarea
    id: suggested_fix
    attributes:
      label: 🔨 Suggested Fix or Action
      description: Suggest what we should do (e.g., remove, redact, archive, warn author).
      placeholder: Recommend archiving the post and flagging for future review.
    validations:
      required: false

  - type: textarea
    id: extra_notes
    attributes:
      label: 🧠 Additional Context
      description: Links to sources, screenshots, references, or any other relevant information.
      placeholder: You can add external sources, screenshots, or explain deeper context here.
    validations:
      required: false

  - type: checkboxes
    id: code_of_conduct
    attributes:
      label: Code of Conduct
      description: By submitting this report, you agree to follow our [Code of Conduct](https://github.com/zunalita/.github/blob/main/CODE_OF_CONDUCT.md)
      options:
        - label: I agree to follow the Code of Conduct and submit this report in good faith.
          required: true
