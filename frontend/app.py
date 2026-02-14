import streamlit as st
import requests
st.title("Code Documentation Navigator")
if "repo_loaded" not in st.session_state:
    st.session_state.repo_loaded = False
repo = st.text_input("GitHub Repo URL")
if st.button("Load Repo"):
    if repo.strip() == "":
        st.warning("Please enter repository URL")
    else:
        with st.spinner("Indexing repository..."):
            try:
                res = requests.post(
                    "http://localhost:8000/load",
                    params={"url": repo}
                )
                if res.status_code == 200:
                    st.session_state.repo_loaded = True
                    st.success("Repository indexed successfully!")
                else:
                    st.error("Failed to index repository")
            except Exception as e:
                st.error(f"Backend not reachable: {e}")
st.markdown("---")
query = st.text_input("Ask about code")
ask_disabled = not st.session_state.repo_loaded
if st.button("Ask", disabled=ask_disabled):
    with st.spinner("Searching codebase..."):
        try:
            res = requests.post(
                "http://localhost:8000/ask",
                params={"query": query}
            )
            if res.status_code != 200:
                st.error("Backend error")
            else:
                response = res.json()
                if "error" in response:
                    st.error(response["error"])
                else:
                    st.markdown("## Answer")
                    st.write(response["answer"])
                    for ctx in response["contexts"]:
                        st.markdown("### File")
                        st.write(ctx["file"])
                        st.markdown("**Complexity Score:**")
                        st.write(ctx.get("complexity", 0))
                        st.markdown("**Risk Alerts:**")
                        st.write(ctx.get("risks", []))
                        st.markdown("**Change Risk Level:**")
                        st.write(ctx.get("change_risk", "UNKNOWN"))
                        st.markdown("**Dependency Impact:**")
                        st.write(
                            ctx.get(
                                "dependency_impact",
                                "Changing this file may impact imported modules."
                            )
                        )
                        st.info("Context retrieved successfully.")
        except Exception as e:
            st.error(f"Request failed: {e}")
