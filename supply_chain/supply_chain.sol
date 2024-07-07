// supply_chain.sol
pragma solidity ^0.6.0;

contract SupplyChain {
  address private owner;
  mapping (address => uint256) public balances;

  constructor() public {
    owner = msg.sender;
  }

  function addProduct(string memory _productName, uint256 _quantity) public {
    // Add product to supply chain
    balances[msg.sender] += _quantity;
  }

  function transferProduct(address _recipient, uint256 _quantity) public {
    // Transfer product to recipient
    balances[msg.sender] -= _quantity;
    balances[_recipient] += _quantity;
  }

  function getProductBalance(address _address) public view returns (uint256) {
    // Get product balance for address
    return balances[_address];
  }
}
