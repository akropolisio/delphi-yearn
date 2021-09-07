import os
import pytest
from brownie import accounts
from brownie import Contract
import sys
from utils.deploy_helpers import deploy_proxy, deploy_admin
from web3 import Web3, HTTPProvider


node = 'https://mainnet.infura.io/v3/8dd752f655754f9cacbe55ca32427737'

web3  = Web3(HTTPProvider(node))


from dotenv import load_dotenv, find_dotenv


@pytest.fixture(scope="module")
def env_settings():
    yield load_dotenv(find_dotenv())

@pytest.fixture
def deployer():
    yield accounts[0]

@pytest.fixture
def dai(env_settings):
    dai_token = Contract.from_explorer(os.getenv("DAI"), as_proxy_for=None)
    yield dai_token


@pytest.fixture()
def crv(env_settings):
    crv_token = Contract.from_explorer(os.getenv("CRV"), as_proxy_for=None)
    yield crv_token


@pytest.fixture
def weth(env_settings):
    weth_address= Contract.from_explorer(os.getenv("WETH"), as_proxy_for=None)
    yield weth_address

@pytest.fixture(scope="module")
def user1():
    yield accounts[1]


@pytest.fixture(scope="module")
def user2():
    yield accounts[2]

@pytest.fixture(scope="function")
def curveRegistry():
    registry = Contract.from_explorer(os.getenv("CURVEREG"), as_proxy_for=None)
    yield registry

@pytest.fixture
def zap(deployer, Zap):
    registry = Contract.from_explorer(os.getenv("CURVEREG"), as_proxy_for=None)
    zapContract = deployer.deploy(Zap, registry)
    yield zapContract

@pytest.fixture
def dai_owner():
    yield accounts.at("0x47ac0fb4f2d84898e4d9e7b4dab3c24507a6d503", force=True)


@pytest.fixture
def akro():
    akro_token = Contract.from_explorer(os.getenv("MAINNET_AKRO_TOKEN"), as_proxy_for=None)
    yield akro_token

@pytest.fixture
def usdt():
    usdt_token = Contract.from_explorer(os.getenv("MAINNET_USDT"), as_proxy_for=None)
    yield usdt_token


@pytest.fixture
def curve_swap_address():
    swapAddress = Contract.from_explorer(os.getenv("TRICRYPTO_SWAP_ADDRESS"), as_proxy_for=None)
    yield swapAddress

@pytest.fixture
def curve_token():
    token = Contract.from_explorer(os.getenv("TRICRYPTO_TOKEN"), as_proxy_for=None)
    yield token


@pytest.fixture(scope="module")
def akro_owner():
    owner = accounts.at(os.getenv("MAINNET_AKRO_HOLDER"), force=True)
    yield owner


@pytest.fixture
def target():
    
    abi=[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"bytes4","name":"selector","type":"bytes4"}],"name":"getFunctionImplementation","outputs":[{"internalType":"address","name":"impl","type":"address"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]
    address1 = "0xDef1C0ded9bec7F1a1670819833240f027b25EfF"
    targetTocheck = Contract.from_abi("ZeroEx", address1, abi=abi)
    yield targetTocheck



@pytest.fixture
def weth_owner():
    owner = accounts.at("0x08638ef1a205be6762a8b935f5da9b700cf7322c", force=True)
    yield owner