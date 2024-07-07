pragma solidity ^0.8.0;

contract TheBlockChainMessenger {
    address private owner;
    string public message;
    uint public updateCount;

    constructor() {
        owner = msg.sender;
        message = "";
        updateCount = 0;
    }

    function updateMessage(string memory _message) public {
        require(msg.sender == owner, "Only the owner can update the message");
        message = _message;
        updateCount++;
    }

    function getMessage() public view returns (string memory) {
        return message;
    }

    function getUpdateCount() public view returns (uint) {
        return updateCount;
    }
}
