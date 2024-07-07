pragma solidity ^0.8.0;

contract TheFarmNFT {
    address private owner;
    string public name;
    string public symbol;
    uint public totalSupply;

    constructor() {
        owner = msg.sender;
        name = "FarmNFT";
        symbol = "FNFT";
        totalSupply = 100;
    }

    function mint(address _to, string memory _uri) public {
        require(msg.sender == owner, "Only the owner can mint NFTs");
        require(totalSupply < 100, "Maximum NFT supply reached");
        totalSupply++;
        _to.mint(_uri);
    }

    function ownerOf(uint _tokenId) public view returns (address) {
        return _tokenId.owner;
    }
}
