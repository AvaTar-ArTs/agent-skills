"""Tests for scripts/common/secrets.py"""
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from common.secrets import redact, assert_no_secrets


def test_redact_openai_key():
    text = "key: sk-proj-abcdefghijklmnopqrstuvwxyz1234567890"
    assert '[REDACTED]' in redact(text)
    assert 'sk-proj' not in redact(text)


def test_redact_replicate_key():
    text = "REPLICATE_API_TOKEN=r8_abcdefghijklmnopqrstuvwxyz"
    result = redact(text)
    assert '[REDACTED]' in result


def test_redact_bearer_token():
    text = "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9abc"
    assert '[REDACTED]' in redact(text)


def test_redact_private_key():
    text = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBg..."
    assert '[REDACTED]' in redact(text)


def test_redact_leaves_clean_text():
    text = "Hello world, this is a normal prompt with no secrets."
    assert redact(text) == text


def test_assert_no_secrets_raises_on_key():
    with pytest.raises(ValueError, match="Secret-looking"):
        assert_no_secrets("sk-ant-api03-abcdefghijklmnopqrstuvwxyz12345678")


def test_assert_no_secrets_passes_clean():
    assert_no_secrets("A clean prompt with no secrets here.")
