// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

contract GarbageCollectorMonitoring
{
    struct GarbageBin
    {
        bool isRegistered;
        uint256 lastCollectedAt;
        uint256 lastCollectedWeight;
        uint256 lastFilledAt;
        uint256 currentWeight;
        uint256 latitude;
        uint256 longitude;
    }

    // first uint256 is for Latitude and second uint256 is for Longitude
    mapping(uint256 => mapping(uint256 => GarbageBin)) public garbageBinsByLatLong;

    event GarbageBinFilled(uint256 indexed latitude, uint256 indexed longitude, string message);
    event GarbageBinEmptied(uint256 indexed latitude, uint256 indexed longitude, string message);
    event GarbageBinWeightUpdated(uint256 indexed latitude, uint256 indexed longitude, uint256 newWeight);

    modifier onlyRegisteredBin(uint256 latitude, uint256 longitude)
    {
        require(garbageBinsByLatLong[latitude][longitude].isRegistered, "Garbage bin not registered");
        _;
    }

    function viewGarbageBinByLatLong(uint256 latitude, uint256 longitude) public view returns(GarbageBin memory)
    {
        // Direct check instead of modifier call
        require(garbageBinsByLatLong[latitude][longitude].isRegistered, "Garbage bin not registered");
        return garbageBinsByLatLong[latitude][longitude];
    }

    function registerGarbageBin(uint256 latitude, uint256 longitude) public
    {
        require(!garbageBinsByLatLong[latitude][longitude].isRegistered, "Garbage bin already registered");
        garbageBinsByLatLong[latitude][longitude] = GarbageBin(true, 0, 0, 0, 0, latitude, longitude);
    }

    function reportFilledByLatLong(uint256 latitude, uint256 longitude) public onlyRegisteredBin(latitude, longitude)
    {
        emit GarbageBinFilled(latitude, longitude, "Filled");
        garbageBinsByLatLong[latitude][longitude].lastFilledAt = block.timestamp;
    }

    function reportEmptiedByLatLong(uint256 latitude, uint256 longitude) public onlyRegisteredBin(latitude, longitude)
    {
        emit GarbageBinEmptied(latitude, longitude, "Emptied");
        garbageBinsByLatLong[latitude][longitude].lastCollectedAt = block.timestamp;
        garbageBinsByLatLong[latitude][longitude].lastCollectedWeight = garbageBinsByLatLong[latitude][longitude].currentWeight;
        garbageBinsByLatLong[latitude][longitude].currentWeight = 0;
    }

    function timeSinceLastFilled(uint256 latitude, uint256 longitude) public view onlyRegisteredBin(latitude, longitude) returns(uint256)
    {
        return block.timestamp - garbageBinsByLatLong[latitude][longitude].lastFilledAt;
    }

    function getWeightOfGarbageBinByLatLong(uint256 latitude, uint256 longitude) public view onlyRegisteredBin(latitude, longitude) returns(uint256)
    {
        return garbageBinsByLatLong[latitude][longitude].currentWeight;
    }

    function setWeightOfGarbageBinByLatLong(uint256 latitude, uint256 longitude, uint256 weight) public onlyRegisteredBin(latitude, longitude)
    {
        garbageBinsByLatLong[latitude][longitude].currentWeight = weight;
        emit GarbageBinWeightUpdated(latitude, longitude, weight);
    }
}
