# Switching the GitHub account Claude uses

This repo lives under the **`defencelab-interactive`** account. Several other projects live
under **`cyber-learning-interactives`** (`clinic-demo`, `harness-interactives/bridge-course`,
`Python-interactives/Python-Foundation` and a few personal repos).

Claude can only be authorised to **one GitHub account at a time**. Whichever one is connected
decides which repositories a Claude Code session can push to. Switching to work on this repo
cuts off the others, and vice versa — so this will come up again.

---

## The symptom

A push fails with:

```
remote: access denied by the git proxy: defencelab-interactive/Practical-Cybersecurity-for-the-Modern-Workplace
is not in this session's authorized repository set, so the proxy will not inject a credential for it.
fatal: ... The requested URL returned error: 403
```

**This is not a token problem.** A personal access token in the remote URL will not help, and
neither will creating a new one — the request is refused inside the session before it reaches
GitHub. The same error appears with a completely made-up token, which is how to tell the two
apart.

It is also not a permissions problem on GitHub. The Claude GitHub App is installed on
`defencelab-interactive` with **All repositories** and read/write access to code. That side is
fine and does not need changing.

The cause is that Claude is authorised under the *other* account.

---

## Confirming it in ten seconds

In **claude.ai → Settings → Customize → Connectors → GitHub Integration**, look at the
*Claude GitHub App* block. It lists the accounts Claude can currently see. If
`defencelab-interactive` is not in that list, that is the problem.

Below it, *Check repository status* takes an `owner/repo` and answers directly. Typing
`defencelab-interactive/Practical-Cybersecurity-for-the-Modern-Workplace` returns either:

- ✅ *Claude Code cloud sessions can work in …* — connected correctly, the problem is elsewhere
- ⚠️ *The Claude GitHub App on defencelab-interactive isn't connected. Your connected GitHub
  account can't see defencelab-interactive's repositories.* — wrong account

---

## Switching

1. Open **claude.ai → Settings → Customize → Connectors → GitHub Integration**
2. Scroll to *Check repository status* and click **Switch GitHub account**
3. GitHub opens an authorisation page. **Make sure the browser is logged into the account you
   want.** The page shows *Signed in as …* — if that is the right one, click **Continue**.
   If not, use *Use a different account* and sign in first.
4. The tab closes itself. The connector panel should now list the new account as *Installed*.
5. In the Claude Code session, the repo still needs attaching once — ask Claude to add it, or
   it will do so on the next push attempt. It then clones to a fresh directory
   (`/home/claude/<repo-name>`) and pushes from there.

Switching back is the same flow in reverse. The catch: **the browser has to be signed into the
target GitHub account**, so going back to `cyber-learning-interactives` means signing out of
`defencelab-interactive` in GitHub first. Claude cannot do that step — it will not enter
passwords.

---

## What does not fix it

- **A new personal access token.** The refusal happens before GitHub sees the token.
- **"Install on another account"** in the connector panel. It opens the GitHub install page for
  the account the *browser* is signed into — if the app is already installed there, nothing
  changes. The blocker is the authorised account, not the installation.
- **Accepting the pending permission update.** The request (as of Nov 2026) asks for read access
  to Administration and Merge queues plus repository creation. None of that is needed for
  pushing; `Contents: read & write` is what matters and the app already has it. GitHub keeps the
  app's current permissions if the request is declined.

---

## Session notes

- The set of pushable repos is fixed **when a session starts**. If the account changes while a
  session is running, that session keeps the old set — a restart picks up the new one.
- After a container restart the working copy is gone. Clone again before continuing.
- A session can read any public repo regardless of all this. Only pushing is gated.
- Pages rebuilds on its own after a push; it usually takes under a minute. The container cannot
  reach `github.io` to verify, so check the published page in a browser.
