#!/bin/bash
uvicorn --reload api:app --host 0.0.0.0 --port=8080
