name: 🛑 Malicious or Misleading Post
description: Report a post that contains false information, security risks, or violates guidelines.
title: "Potential Vulnerable Post: [FILENAME].md"
labels: ['malicious-post']
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        ⚠️ **Use this form to report any post that may be misleading, dangerous, or malicious.**  
        We'll review it within **72 hours** and either archive the post or reply with reasoning.

  - type: input
    id: file_url
    attributes:
      label: 🔗 Post URL
      description: Link to the file in `/posts` (e.g. https://github.com/org/zunalita/blob/main/posts/xx-xx-xxxx-malicious.md)
      placeholder: https://github.com/zunalita/posts/blob/main/posts/xx-xx-xxxx-malicious.md
    validations:
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
      label: 📄 Description
      description: Clearly explain what the issue is. For malicious code, mention the line number or section.
      placeholder: |
        The post contains JavaScript that auto-executes downloads...
        Or: This post encourages unsafe behavior by recommending...
    validations:
      required: true

  - type: textarea
    id: suggested_fix
    attributes:
      label: 🔨 Suggested Fix or Action
      description: Suggest how we should fix or handle this (e.g., remove file, redact section, archive, etc.)
      placeholder: Redact the post...
    validations:
      required: false

  - type: textarea
    id: extra_notes
    attributes:
      label: 🧠 Additional Notes
      description: Add any related links, context, screenshots, or other relevant info.
      placeholder: Source links, screenshots, etc.
    validations:
      required: false
