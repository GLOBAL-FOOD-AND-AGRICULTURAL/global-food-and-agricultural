pragma solidity ^0.8.0;

contract TheFarmToken {
    address private owner;
    string public name;
    string public symbol;
    uint public totalSupply;

    constructor() {
        owner = msg.sender;
        name = "FarmToken";
        symbol = "FT";
        totalSupply = 1000000;
    }

    function transfer(address _to, uint _value) public {
        require(msg.sender == owner, "Only the owner can transfer tokens");
        require(_value <= totalSupply, "Insufficient tokens");
        totalSupply -= _value;
        _to.transfer(_value);
    }

    function balanceOf(address _owner) public view returns (uint) {
        return _owner.balance;
    }
}
