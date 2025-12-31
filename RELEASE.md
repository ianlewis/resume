# Release Guide

This document outlines the steps to follow when preparing and executing a new
release.

1. Create a new tag for the release.

    ```bash
    git tag YYYY.MM.DD
    git push origin YYYY.MM.DD
    ```

2. The `create.release.yml` GitHub Action will automatically run and create a
   new release draft based on the new tag and upload the release assets.
3. Review the release draft and update the release notes.
4. Publish the release.
