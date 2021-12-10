<link rel="stylesheet" type="text/css" href="css/admin.css">

<div class="admin">
    <!-- Admin Page -->
    <!-- Allows admin user to delete, mute users -->
    %if user_type == 'admin':
        <h1>Welcome back ADMIN</h1>
        <div>
            <h2>User List</h2>
                <ul class="user-list">
                %for item in users:
                    <li>
                        <div class="user-row">
                            <div class="row-section">
                                <h3 id="targer-username">{{item}}</h3>
                            </div>
                            
                            <div class="row-section">
                                <form action="/unmuteuser" method="POST">
                                    <input type="hidden"  value="{{item}}" name="target-user">
                                    <button class="adminBtn" id="unmuteBtn" type="submit">Unmute</button>
                                    <input hidden name="page_token" value="(pageToken)">
                                </form>
                            </div>

                            <div class="row-section">
                                <form action="/muteuser" method="POST">
                                    <input type="hidden"  value="{{item}}" name="target-user">
                                    <button class="adminBtn" id="muteBtn" type="submit">Mute</button>
                                    <input hidden name="page_token" value="(pageToken)">
                                </form>
                            </div>
                            
                            <div class="row-section">
                                <form action="/deleteuser" method="POST">
                                    <input type="hidden"  value="{{item}}" name="target-user">
                                    <button class="adminBtn" id="deleteBtn">Delete</button>
                                    <input hidden name="page_token" value="(pageToken)">
                                </form>
                            </div>
                        </div>
                    </li>
                %end
                </ul>
        </div>
    %else:
        <h2>Do not have access to this page</h2>
    %end

</div>
